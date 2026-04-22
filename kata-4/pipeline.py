# pipeline
import pandas as pd
import numpy as np
from unidecode import unidecode
import re, os, json
from datetime import datetime

def parse_data(valor):
    # normaliza datas em formatos mistos para datetime
    if pd.isna(valor) or str(valor).strip() == "":
        return pd.NaT
    s = str(valor).strip()
    formatos = [
        "%Y-%m-%d", "%d/%m/%Y",
        "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M:%S",
    ]
    for fmt in formatos:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return pd.NaT


def parse_valor(valor):
    # normaliza valores monetários com vírgula ou ponto decimal
    if pd.isna(valor) or str(valor).strip() == "":
        return np.nan
    s = str(valor).strip()
    # remove pontos de milhar quando há vírgula decimal: "2.300,50" to 2300.50
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return np.nan


def normalizar_cidade(cidade):
    # padroniza grafias de cidades: remove acentos inconsistentes, aplica title case
    if pd.isna(cidade) or str(cidade).strip() == "":
        return "Desconhecida"
    # unidecode remove acentos e normaliza encoding, depois title case
    return unidecode(str(cidade).strip()).title()


# 2 - leitura

print("=" * 60)
print("PIPELINE DE TRANSFORMAÇÃO LOGÍSTICA")
print("=" * 60)

pedidos  = pd.read_csv("dados/pedidos.csv",  dtype=str)
clientes = pd.read_csv("dados/clientes.csv", dtype=str)
entregas = pd.read_csv("dados/entregas.csv", dtype=str)

print(f"\n[LEITURA] pedidos={len(pedidos)} | clientes={len(clientes)} | entregas={len(entregas)}")

# 3 - limpeza - pedidos

pedidos["data_pedido"]  = pedidos["data_pedido"].apply(parse_data)
pedidos["valor_total"]  = pedidos["valor_total"].apply(parse_valor)

nulos_data  = pedidos["data_pedido"].isna().sum()
nulos_valor = pedidos["valor_total"].isna().sum()
print(f"\n[PEDIDOS] datas nulas descartadas: {nulos_data} | valores nulos: {nulos_valor}")

# remove registros sem data
pedidos = pedidos.dropna(subset=["data_pedido"])

# valor nulo => 0 (pedidos cancelados sem valor registrado)
pedidos["valor_total"] = pedidos["valor_total"].fillna(0.0)

# 4 - limpeza - clientes

clientes["data_cadastro"]     = clientes["data_cadastro"].apply(parse_data)
clientes["cidade_normalizada"] = clientes["cidade"].apply(normalizar_cidade)
clientes["estado"]             = clientes["estado"].str.strip().str.upper()

print(f"\n[CLIENTES] cidades normalizadas (amostras):")
for _, r in clientes.iterrows():
    if r["cidade"] != r["cidade_normalizada"]:
        print(f"   '{r['cidade']}' → '{r['cidade_normalizada']}'")

# 5 - limpeza - entrega

entregas["data_prevista"]  = entregas["data_prevista"].apply(parse_data)
entregas["data_realizada"] = entregas["data_realizada"].apply(parse_data)

# Detecta órfãos (id_pedido sem correspondência em pedidos)
ids_validos = set(pedidos["id_pedido"])
orfaos = entregas[~entregas["id_pedido"].isin(ids_validos)]
print(f"\n[ENTREGAS] registros órfãos removidos: {len(orfaos)}")
if not orfaos.empty:
    print(f"   id_pedido órfãos: {orfaos['id_pedido'].tolist()}")

entregas_clean = entregas[entregas["id_pedido"].isin(ids_validos)].copy()

# calcula atraso dos dias
def calc_atraso(row):
    if pd.isna(row["data_realizada"]):
        return np.nan  # ainda não entregue
    return (row["data_realizada"] - row["data_prevista"]).days

entregas_clean["atraso_dias"] = entregas_clean.apply(calc_atraso, axis=1)

# 6 - consolidacao

# pega 1 entrega por pedido (a mais recente em caso de duplicatas)
entrega_por_pedido = (
    entregas_clean
    .sort_values("data_prevista")
    .drop_duplicates("id_pedido", keep="last")
    [["id_pedido","data_prevista","data_realizada","atraso_dias","status_entrega"]]
)

merged = (
    pedidos
    .merge(clientes[["id_cliente","nome","cidade_normalizada","estado"]], on="id_cliente", how="left")
    .merge(entrega_por_pedido, on="id_pedido", how="left")
)

# renomeia para schema final
consolidado = merged.rename(columns={
    "nome":           "nome_cliente",
    "status":         "status_pedido",
    "data_prevista":  "data_prevista_entrega",
    "data_realizada": "data_realizada_entrega",
})[["id_pedido","nome_cliente","cidade_normalizada","estado","valor_total",
    "status_pedido","data_pedido","data_prevista_entrega",
    "data_realizada_entrega","atraso_dias","status_entrega"]]

os.makedirs("saida", exist_ok=True)
consolidado.to_csv("saida/consolidado.csv", index=False, date_format="%Y-%m-%d")
print(f"\n[CONSOLIDADO] {len(consolidado)} registros → saida/consolidado.csv")

# 7 - indicadores

print("\n" + "=" * 60)
print("INDICADORES DE DESEMPENHO")
print("=" * 60)

# 7.1 total de pedidos por status
print("\n PEDIDOS POR STATUS")
status_counts = consolidado["status_pedido"].value_counts()
for status, qtd in status_counts.items():
    print(f"   {status:<15} {qtd:>3} pedido(s)")

# 7.2 ticket médio por estado
print("\n TICKET MÉDIO POR ESTADO")
ticket_estado = (
    consolidado[consolidado["valor_total"] > 0]
    .groupby("estado")["valor_total"]
    .mean()
    .sort_values(ascending=False)
)
for estado, media in ticket_estado.items():
    print(f"   {estado}  R$ {media:,.2f}")

# 7.3 % no prazo vs. com atraso
entregues = consolidado[consolidado["atraso_dias"].notna()]
total_e = len(entregues)
no_prazo  = (entregues["atraso_dias"] <= 0).sum()
atrasadas = (entregues["atraso_dias"] >  0).sum()
print(f"\n PONTUALIDADE DAS ENTREGAS (base: {total_e} entregas concluídas)")
print(f"   No prazo / antecipadas : {no_prazo:>3}  ({no_prazo/total_e*100:.1f}%)")
print(f"   Com atraso             : {atrasadas:>3}  ({atrasadas/total_e*100:.1f}%)")

# 7.4 top 3 cidades por volume de pedidos
print("\n  TOP 3 CIDADES POR VOLUME DE PEDIDOS")
top3 = (
    consolidado["cidade_normalizada"]
    .value_counts()
    .head(3)
)
for i, (cidade, qtd) in enumerate(top3.items(), 1):
    print(f"   {i}. {cidade:<20} {qtd} pedido(s)")

# 7.5 media de atraso para pedidos com atraso
atrasados_df = consolidado[consolidado["atraso_dias"] > 0]
media_atraso = atrasados_df["atraso_dias"].mean()
print(f"\n MÉDIA DE ATRASO (pedidos atrasados): {media_atraso:.1f} dias")

# salva indicadores em JSON
indicadores = {
    "pedidos_por_status": status_counts.to_dict(),
    "ticket_medio_por_estado": {k: round(v,2) for k,v in ticket_estado.items()},
    "pontualidade": {
        "total_entregues": int(total_e),
        "no_prazo_pct": round(no_prazo/total_e*100, 1),
        "atrasadas_pct": round(atrasadas/total_e*100, 1),
    },
    "top3_cidades": top3.to_dict(),
    "media_atraso_dias": round(float(media_atraso), 1),
}
with open("saida/indicadores.json","w",encoding="utf-8") as f:
    json.dump(indicadores, f, ensure_ascii=False, indent=2)

print("\n Pipeline concluído! Arquivos gerados:")
print("   saida/consolidado.csv")
print("   saida/indicadores.json")