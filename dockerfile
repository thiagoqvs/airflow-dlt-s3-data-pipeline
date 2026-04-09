FROM apache/airflow:2.9.1-python3.11

WORKDIR /opt/airflow

RUN pip install --no-cache-dir \
    "dlt[filesystem]" \
    "pandas>=2.2,<2.3" \
    "pyarrow>=15,<17" \
    "python-dotenv>=1.0,<2.0"