from fastapi import APIRouter, HTTPException
from src.services.viz_service import BasicAutoService

router = APIRouter(tags=["Auto Basic Visualizations"])

svc = BasicAutoService()

@router.get("/visualize/{dataset_id}/basic")
def auto_basic_visualizations(dataset_id: str):
    """
    Automatically generates basic charts:
    - histograms for numeric columns
    - bar charts for categorical columns
    - box plots
    - correlation matrix
    """
    try:
        result = svc.generate_basic_visuals(dataset_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
