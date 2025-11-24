from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    category: Optional[str] = None
    unit: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class SalesRecordBase(BaseModel):
    product_id: int
    quantity_sold: float
    date: datetime
    store_id: Optional[int] = None

class SalesRecordCreate(SalesRecordBase):
    pass

class SalesRecordRead(SalesRecordBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class InventoryBase(BaseModel):
    product_id: int
    current_stock: float
    safety_stock: float = 0
    lead_time_days: int = 7
    store_id: Optional[int] = None

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    current_stock: Optional[float] = None
    safety_stock: Optional[float] = None
    lead_time_days: Optional[int] = None

class InventoryRead(InventoryBase):
    id: int
    updated_at: datetime
    
    class Config:
        from_attributes = True

class InventoryRecommendation(BaseModel):
    product_id: int
    current_stock: float
    recommended_stock: float
    reorder_point: float
    risk_level: str  # "Understock", "Optimal", "Overstock"
    forecasted_demand: float
    forecast_horizon: int

class ForecastBase(BaseModel):
    product_id: int
    forecast_date: datetime
    forecasted_demand: float
    confidence: Optional[float] = None
    model_version: Optional[str] = None
    store_id: Optional[int] = None

class ForecastCreate(ForecastBase):
    pass

class ForecastRead(ForecastBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ForecastResponse(BaseModel):
    product_id: int
    forecasts: List[dict]
    horizon_days: int
    avg_forecast: float
    confidence: float

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
