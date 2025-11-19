from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.MeasurementResponse)
def create_measurement(data: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    baby = db.query(models.Baby).filter(models.Baby.id == data.baby_id).first()
    if not baby:
        raise HTTPException(status_code=404, detail="Baby not found")

    new_m = models.Measurement(**data.dict())
    db.add(new_m)
    db.commit()
    db.refresh(new_m)
    return new_m


@router.get("/", response_model=list[schemas.MeasurementResponse])
def list_measurements(db: Session = Depends(get_db)):
    return db.query(models.Measurement).all() 
