from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class FilterSpec(BaseModel):
    col: str
    op: str  
    value: Any

class BaseVizRequest(BaseModel):
    filters: Optional[list[FilterSpec]] = Field(default=None, description="List of filters to apply")
   

class BarRequest(BaseVizRequest):
    x: str
    y: Optional[str] = None 
    agg: Optional[str] = "count"  
    group_by: Optional[str] = None 
    limit: Optional[int] = 50

class LineRequest(BaseVizRequest):
    x: str 
    y: str
    agg: Optional[str] = "sum"
    time_granularity: Optional[str] = None  

class PieRequest(BaseVizRequest):
    category: str
    value: Optional[str] = None  
    top_n: Optional[int] = 10

class HistogramRequest(BaseVizRequest):
    column: str
    bins: Optional[int] = 10
    range: Optional[list] = None 

class AreaRequest(BaseVizRequest):
    x: str
    y: str
    agg: Optional[str] = "sum"
    group_by: Optional[str] = None
