import os
import pandas as pd
from typing import Optional

DATASET_DIR = os.path.join(os.path.dirname(__file__), "..", "storage", "datasets")

os.makedirs(DATASET_DIR, exist_ok=True)

def dataset_path(dataset_id: str) -> str:
   
    return os.path.join(DATASET_DIR, f"{dataset_id}.parquet")

def load_dataset(dataset_id: str) -> pd.DataFrame:
    path = dataset_path(dataset_id)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset {dataset_id} not found at {path}")
   
    df = pd.read_parquet(path)
    return df
