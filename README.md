🚀 Pipeline de Dados com Airflow, dlt e MinIO (S3)
Pipeline de dados completo simulando um cenário real de engenharia de dados. O projeto realiza a ingestão automatizada de dados de câmbio via API, processa e armazena em um Data Lake local no formato Parquet, com orquestração via Apache Airflow.

🏗️ Arquitetura
FreeCurrency API
      │
      ▼
 dlt (ingestão)
      │
      ▼
Apache Airflow (orquestração via DAG)
      │
      ▼
  MinIO / S3 (Data Lake)
      │
      ▼
Arquivos Parquet

🛠️ Tecnologias utilizadas
FerramentaFinalidadePythonLinguagem principalApache AirflowOrquestração do pipeline via DAGsdlt (data load tool)Ingestão e carga de dadosMinIOData Lake local (compatível com S3)Docker / Docker ComposeContainerização do ambientePandasManipulação de dadosPyArrowEscrita em formato Parquet

⚙️ Funcionalidades

✅ Ingestão automatizada de dados via API (FreeCurrency)
✅ Orquestração com Apache Airflow (DAG com execução horária)
✅ Armazenamento em Data Lake simulado com MinIO (S3)
✅ Dados persistidos em formato Parquet (eficiente e escalável)
✅ Ambiente 100% containerizado com Docker


📁 Estrutura do projeto
airflow-dlt-s3-data-pipeline/
│
├── dags/
│   └── currency_ingestion_dag.py   # DAG principal do Airflow
│
├── ingestion/
│   ├── pipeline.py                 # Configuração do pipeline dlt
│   └── source.py                   # Fonte de dados (FreeCurrency API)
│
├── scripts/
│   └── ready_parquet.py            # Leitura e validação dos arquivos Parquet
│
├── data/
│   └── latest/                     # Dados mais recentes ingeridos
│
├── docker-compose.yaml             # Orquestração dos containers
├── dockerfile                      # Imagem customizada do Airflow
├── pyproject.toml                  # Dependências do projeto
└── README.md

▶️ Como executar o projeto
Pré-requisitos

Docker instalado
Docker Compose instalado

Passo a passo
1. Clone o repositório:
bashgit clone https://github.com/thiagoqvs/airflow-dlt-s3-data-pipeline.git
cd airflow-dlt-s3-data-pipeline
2. Suba os containers:
bashdocker compose up --build
3. Acesse o Airflow:
URL:   http://localhost:8080
User:  admin
Pass:  admin
4. Ative e execute a DAG:
Nome da DAG: freecurrency_hourly_ingestion
5. Acesse o MinIO para visualizar os dados:
URL:   http://localhost:9001

📊 Sobre os dados
Os dados são coletados da FreeCurrency API, que fornece taxas de câmbio em tempo real. O pipeline coleta, transforma e armazena os dados em formato Parquet particionado por data no bucket do MinIO.

🧠 Aprendizados e decisões técnicas

MinIO foi escolhido por ser compatível com a API do S3, permitindo simular um ambiente de cloud localmente
dlt simplifica a ingestão de dados sem necessidade de boilerplate code
Parquet foi escolhido por ser um formato colunar, eficiente para análises posteriores
Docker Compose garante que o ambiente seja reproduzível em qualquer máquina


👤 Autor
Thiago Victorino
