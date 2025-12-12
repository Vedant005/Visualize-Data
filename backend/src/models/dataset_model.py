from pydantic import BaseModel
from typing import List, Any, Dict

class DatasetMetadata(BaseModel):
    rows: int
    columns: int
    column_names: list[str]
    dtypes: dict
    original_columns: list[str]

class DatasetUploadResponse(BaseModel):
    dataset_id: str
    message: str
    metadata: DatasetMetadata
    name: str
