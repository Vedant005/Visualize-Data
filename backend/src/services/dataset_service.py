import os
import uuid
import pandas as pd
from src.utils.fileProcessing import load_dataset
from src.utils.preprocess import preprocess_dataframe

DATASET_DIR = "src/storage/datasets"

def process_and_store_dataset(file_bytes:bytes, filename: str, dataset_name: str):

    os.makedirs(DATASET_DIR, exist_ok=True)

    df = load_dataset(file_bytes, filename)

    # Preprocess the dataset
    clean_df, metadata = preprocess_dataframe(df)

    # Unique ID for this dataset
    dataset_id = str(uuid.uuid4())

    filepath = os.path.join(DATASET_DIR, f"{dataset_id}.parquet")

    clean_df.to_parquet(filepath)

    return {
        "dataset_id": dataset_id,
        "message": "Dataset uploaded and processed successfully.",
        "metadata": metadata,
        "name": dataset_name or filename,
    }



# def process_and_store_dataset(file_bytes: bytes, filename: str, dataset_name: str):

#     # 1️⃣ Load into pandas
#     df = load_dataset(file_bytes, filename)

#     # 2️⃣ Create dataset ID
#     dataset_id = str(uuid.uuid4())[:10]

#     # 3️⃣ Store dataset to filesystem as Parquet (efficient)
#     filepath = f"{DATASET_DIR}/{dataset_id}.parquet"
#     df.to_parquet(filepath)

#     # 4️⃣ Prepare metadata response
#     response = {
#         "dataset_id": dataset_id,
#         "name": dataset_name or filename,
#         "columns": df.columns.tolist(),
#         "rows": len(df),
#         "sample": df.head().to_dict(orient="records"),
#         "message": "Dataset uploaded successfully"
#     }

#     return response