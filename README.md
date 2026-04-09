# airflow-dlt-s3-data-pipeline

# Pipeline de Dados com Airflow, dlt e MinIO (S3)

Este projeto implementa um pipeline de dados completo, simulando um cenário real de engenharia de dados.

A pipeline realiza a ingestão de dados de uma API de câmbio (FreeCurrency API), processa os dados e armazena em um data lake no formato Parquet utilizando MinIO (S3 local), com orquestração via Apache Airflow.

## 🏗️ Arquitetura

Fluxo do pipeline:

API (FreeCurrency)
    ↓
dlt (extração e carga)
    ↓
Apache Airflow (orquestração)
    ↓
MinIO (S3 - Data Lake)
    ↓
Arquivos em formato Parquet

## 🚀 Tecnologias utilizadas

- Python
- Apache Airflow
- dlt (data load tool)
- MinIO (S3 local)
- Docker / Docker Compose
- Pandas
- PyArrow

- ## ⚙️ Funcionalidades

- Ingestão de dados via API (FreeCurrency)
- Orquestração de pipeline com Airflow
- Armazenamento em Data Lake (MinIO)
- Escrita em formato Parquet
- Execução automatizada via DAG

- ## 📁 Estrutura do projeto
projeto-01-ingestao/
│
├── dags/
│   └── currency_ingestion_dag.py
│
├── ingestion/
│   ├── pipeline.py
│   └── source.py
│
├── scripts/
│   └── ready_parquet.py
│
├── docker-compose.yaml
├── Dockerfile
├── .env
└── README.md

## ▶️ Como executar o projeto

1. Clonar o repositório:
```bash
git clone <seu-repo>

2. Subir Containers
docker compose up --build

3. Acessar o Airflow:
http://localhost:8080
Login:
user: admin
senha: admin

4. Executar a DAG:
freecurrency_hourly_ingestion

## 📌 Resultado
```markdown
## 📊 Resultado

Os dados são armazenados no MinIO em formato Parquet, simulando um data lake.

É possível visualizar os arquivos através da interface web do MinIO:
http://localhost:9001

## 🔄 Próximos passos

- Integração com Data Warehouse (MySQL / PostgreSQL)
- Camada de transformação (ELT)
- Visualização com Power BI
- Deploy em ambiente cloud (AWS S3 / MWAA)
