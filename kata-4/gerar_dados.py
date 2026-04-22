"""Gera os três CSVs com sujeiras para o pipeline."""
import csv, os

os.makedirs("dados", exist_ok=True)

# ── pedidos.csv ──────────────────────────────────────────────────────────────
pedidos = [
    ["id_pedido","data_pedido","id_cliente","valor_total","status"],
    ["P001","2024-01-15","C001","1500.00","entregue"],
    ["P002","15/02/2024","C002","2.300,50","processando"],   # data BR + vírgula decimal
    ["P003","2024-03-20 08:30:00","C003","750.00","entregue"],  # timestamp
    ["P004","10/04/2024","C001","","cancelado"],              # valor nulo
    ["P005","2024-05-05","C004","3200.00","entregue"],
    ["P006","20/06/2024","C002","1.100,00","entregue"],
    ["P007","2024-07-01","C005","890.50","processando"],
    ["P008","","C003","450.00","entregue"],                  # data nula
    ["P009","2024-08-10","C001","5600.00","entregue"],
    ["P010","25/09/2024","C006","320.00","cancelado"],
]

# ── clientes.csv ─────────────────────────────────────────────────────────────
clientes = [
    ["id_cliente","nome","cidade","estado","data_cadastro"],
    ["C001","Ana Lima","São Paulo","SP","2023-01-10"],
    ["C002","Bruno Melo","sao paulo","SP","15/03/2023"],    # grafia inconsistente
    ["C003","Carla Souza","RIO DE JANEIRO","RJ","2023-06-01 00:00:00"],  # caixa alta
    ["C004","Diego Costa","Belo Horizonte","MG","20/08/2023"],
    ["C005","Eva Rocha","","RS","2023-09-15"],              # cidade nula
    ["C006","Fábio Nunes","curitiba","PR","2023-11-01"],    # minúscula
]

# ── entregas.csv ─────────────────────────────────────────────────────────────
entregas = [
    ["id_entrega","id_pedido","data_prevista","data_realizada","status_entrega"],
    ["E001","P001","2024-01-20","2024-01-19","entregue"],   # antecipado
    ["E002","P002","20/02/2024","25/02/2024","entregue"],   # 5 dias atraso
    ["E003","P003","2024-03-25","2024-03-25","entregue"],   # no prazo
    ["E004","P005","10/05/2024","15/05/2024","entregue"],   # 5 dias atraso
    ["E005","P006","25/06/2024","2024-06-23","entregue"],   # antecipado
    ["E006","P007","10/07/2024","","em_transito"],          # não entregue
    ["E007","P008","2024-08-20","2024-08-22","entregue"],   # 2 dias atraso
    ["E008","P009","2024-08-20","2024-08-18","entregue"],   # antecipado
    ["E009","P010","2024-10-05","","cancelado"],
    ["E010","P999","2024-12-01","","em_transito"],          #  — id não existe
    ["E011","P888","2024-11-15","2024-11-16","entregue"],   # — id não existe
]

for nome, linhas in [("pedidos",pedidos),("clientes",clientes),("entregas",entregas)]:
    with open(f"dados/{nome}.csv","w",newline="",encoding="utf-8") as f:
        csv.writer(f).writerows(linhas)

print("CSVs gerados em ./dados/")