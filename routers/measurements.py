from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.MeasurementResponse)
def create_measurement(
    measurement: schemas.MeasurementCreate,
    db: Session = Depends(get_db)
):
    new_measurement = models.Measurement(**measurement.dict())
    db.add(new_measurement)
    db.commit()
    db.refresh(new_measurement)
    return new_measurement

@router.get("/", response_model=list[schemas.MeasurementResponse])
def list_measurements(db: Session = Depends(get_db)):
    return db.query(models.Measurement).all() 
