# 🚀 Pipeline de Dados com Airflow, dlt e MinIO (S3)

Este projeto implementa um pipeline de dados completo, simulando um cenário real de engenharia de dados.

A pipeline realiza a ingestão de dados de uma API de câmbio (FreeCurrency API), processa os dados e armazena em um data lake no formato Parquet utilizando MinIO (S3 local), com orquestração via Apache Airflow.

---

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

---

## 🚀 Tecnologias utilizadas

- Python
- Apache Airflow
- dlt (data load tool)
- MinIO (S3 local)
- Docker / Docker Compose
- Pandas
- PyArrow

---

## ⚙️ Funcionalidades

- Ingestão de dados via API (FreeCurrency)
- Orquestração de pipeline com Airflow
- Armazenamento em Data Lake (MinIO)
- Escrita em formato Parquet
- Execução automatizada via DAG

---

## 📁 Estrutura do projeto
