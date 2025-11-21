# src/routes/measurements.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import SessionLocal
from src import models, schemas

router = APIRouter(prefix="/measurements", tags=["Measurements"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.MeasurementResponse)
def create_measurement(measurement: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    # verify baby exists
    baby = db.query(models.Baby).filter(models.Baby.id == measurement.baby_id).first()
    if not baby:
        raise HTTPException(status_code=404, detail="Baby not found")

   # dentro de create_measurement(...)
fever_threshold = 38.0
fever_flag = measurement.temperature >= fever_threshold



@router.get("/", response_model=List[schemas.MeasurementResponse])
def list_measurements(db: Session = Depends(get_db)):
    return db.query(models.Measurement).order_by(models.Measurement.created_at.desc()).all()
@router.post("/", response_model=schemas.MeasurementResponse)
def create_measurement(measurement: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    new = models.Measurement(
        baby_id=measurement.baby_id,
        temperature=measurement.temperature,
        heart_rate=measurement.heart_rate,
        breathing_rate=measurement.breathing_rate,
        fever_fever_flag=measurement.fever_fever_flag,
    )

    db.add(new)
    db.commit()
    db.refresh(new)
    return new 


@router.get("/baby/{baby_id}", response_model=List[schemas.MeasurementResponse])
def list_measurements_for_baby(baby_id: int, db: Session = Depends(get_db)):
    return db.query(models.Measurement).filter(models.Measurement.baby_id == baby_id).order_by(models.Measurement.created_at.desc()).all() 
