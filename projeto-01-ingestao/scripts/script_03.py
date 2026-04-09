import os
import dlt
from script_02 import freecurrency_source

import requests
from dotenv import load_dotenv
from typing import Iterator
from dlt.sources import DltResource
from dlt.destinations import filesystem
from datetime import datetime, timezone
load_dotenv()

BASE_URL = "https://api.freecurrencyapi.com/v1"
DEFAULT_CURRENCIES = "USD,EUR,JPY"
@dlt.resource(name="latest_rates", write_disposition="append")    
def latest_rates(api_key: str, base_currency: str, currencies: str) -> Iterator[dict]:     
    response = requests.get(
        f"{BASE_URL}/latest",
        params={"apikey": api_key, "base_currency": base_currency, "currencies": currencies},
        timeout=30,
    )
    response.raise_for_status()

    data = response.json().get("data", {})
    extracted_at = datetime.now(timezone.utc).isoformat()

    for targed_currency, rate in data.items():
        yield {
            "base_currency": base_currency,
            "targed_currency": targed_currency,
            "rate": rate,
            "extracted_at": extracted_at,
        }

@dlt.source(name="freecurrency")
def freecurrency_source(
    api_key: str,
    base_currency: str = "BRL",
    currencies: str = DEFAULT_CURRENCIES,
) -> DltResource: 
    return latest_rates(api_key=api_key, base_currency=base_currency, currencies=currencies)

endpoint_url = os.getenv("MINIO_ENDPOINT_URL", "http://localhost:9000")

def build_pipeline() -> dlt.Pipeline:
    destination = filesystem(
    bucket_url=os.getenv("MINIO_BUCKET_URL", "s3://latest"),
    credentials={
        "aws_access_key_id": os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
        "aws_secret_access_key": os.getenv("MINIO_SECRET_KEY", "minioadmin"),
        "endpoint_url": endpoint_url,
    },
)

    return dlt.pipeline(
        pipeline_name="freecurrency_pipeline",
        destination=destination,
        dataset_name="latest",
    )
destination = filesystem(
    bucket_url=os.getenv("MINIO_BUCKET_URL", "s3://latest"),
    credentials={
        "aws_access_key_id": os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
        "aws_secret_access_key": os.getenv("MINIO_SECRET_KEY", "minioadmin"),
        "endpoint_url": endpoint_url,
    },
)

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY não encontrada no .env")
pipeline = build_pipeline()
load_info = pipeline.run(freecurrency_source(api_key=api_key), loader_file_format="parquet")
print(load_info)