import pandas as pd

from io import BytesIO

def load_dataset(file_bytes: bytes, filename: str):
    filename = filename.lower()

    if filename.endswith(".csv"):
        return pd.read_csv(BytesIO(file_bytes))

    elif filename.endswith(".json"):
        return pd.read_json(BytesIO(file_bytes))

    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        return pd.read_excel(BytesIO(file_bytes))

    else:
        raise ValueError("Unsupported file format. Use CSV, JSON, or Excel.")
