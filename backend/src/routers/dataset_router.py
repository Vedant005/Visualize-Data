from fastapi import APIRouter, UploadFile, File, Form
from src.services.dataset_service import process_and_store_dataset
from src.models.dataset_model import DatasetUploadResponse

router = APIRouter(prefix="/dataset", tags=["Dataset"])

@router.post("/upload", response_model=DatasetUploadResponse)
async def upload_dataset(
    file: UploadFile = File(...),
    name: str = Form(None)
):
    file_bytes = await file.read()

    result = process_and_store_dataset(
        file_bytes=file_bytes,
        filename=file.filename,
        dataset_name=name
    )

    return result
