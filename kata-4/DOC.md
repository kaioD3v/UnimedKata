
Este projeto implementa um pipeline de dados (ETL) para processamento de informações logísticas a partir de três fontes:

* `pedidos.csv`
* `clientes.csv`
* `entregas.csv`

O sistema realiza:

* Limpeza e padronização de dados
* Tratamento de inconsistências
* Consolidação das informações
* Geração de indicadores de desempenho

---

# Estrutura do Projeto

```
/projeto
 ├── pipeline.py
 ├── gerar_dados.py
 ├── /dados
 └── /saida
```

---

# Pré-requisitos

* Python 3.8+
* Bibliotecas:

  * pandas
  * numpy
  * unidecode

Instale com:

```
pip install pandas numpy unidecode
```

# Como Executar

# 1. Gerar dados de teste

```
python gerar_dados.py
```

Isso criará os arquivos:

```
/dados/pedidos.csv
/dados/clientes.csv
/dados/entregas.csv
```

# 2. Executar o pipeline

```
python pipeline.py
```

# Saídas Geradas

Após a execução, serão criados:

# `saida/consolidado.csv`

Base final consolidada contendo:

* Dados de pedidos
* Informações de clientes
* Status e prazos de entrega

# `saida/indicadores.json`

Arquivo com métricas de desempenho:

* Pedidos por status
* Ticket médio por estado
* Pontualidade das entregas
* Top 3 cidades por volume
* Média de atraso

# Fluxo do Pipeline

1. Leitura dos dados CSV
2. Limpeza e padronização
3. Remoção de inconsistências
4. Cálculo de métricas (ex: atraso)
5. Consolidação das tabelas
6. Geração de indicadores

# Observações

* Registros sem data de pedido são removidos
* Valores nulos são tratados automaticamente
* Entregas sem pedido correspondente são descartadas
* Cidades são normalizadas para evitar inconsistências

# Dados de Teste

O script `gerar_dados.py` cria dados simulados com erros reais, como:

* Datas em formatos diferentes
* Valores monetários inconsistentes
* IDs inválidos
* Campos vazios

Isso permite testar a robustez do pipeline.