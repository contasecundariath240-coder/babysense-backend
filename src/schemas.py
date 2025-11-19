from pydantic import BaseModel
from datetime import datetime


class BabyBase(BaseModel):
    name: str
    birth_date: str
    gender: str


class BabyCreate(BabyBase):
    pass


class BabyResponse(BabyBase):
    id: int

    class Config:
        orm_mode = True


class MeasurementBase(BaseModel):
    baby_id: int
    temperature: float
    heart_rate: int | None = None
    breathing_rate: int | None = None


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementResponse(MeasurementBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True 
