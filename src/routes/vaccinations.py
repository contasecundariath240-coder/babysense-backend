from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database import SessionLocal
from src import models, schemas

router = APIRouter(prefix="/vaccinations", tags=["Vaccinations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.VaccinationResponse)
def create_vaccination(v: schemas.VaccinationCreate, db: Session = Depends(get_db)):
    baby = db.query(models.Baby).filter(models.Baby.id == v.baby_id).first()
    if not baby:
        raise HTTPException(status_code=404, detail="Baby not found")
    new = models.Vaccination(baby_id=v.baby_id, name=v.name, date=v.date, notes=v.notes)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/", response_model=List[schemas.VaccinationResponse])
def list_vaccinations(db: Session = Depends(get_db)):
    return db.query(models.Vaccination).order_by(models.Vaccination.date.desc()).all() 
