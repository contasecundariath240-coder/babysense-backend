# src/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class BabyBase(BaseModel):
    name: str
    birth_date: str
    gender: str


class BabyCreate(BabyBase):
    pass


class BabyResponse(BabyBase):
    id: int

    model_config = {"from_attributes": True}


class MeasurementBase(BaseModel):
    baby_id: int
    temperature: float
    heart_rate: Optional[int] = None
    breathing_rate: Optional[int] = None


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementResponse(MeasurementBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True} 
