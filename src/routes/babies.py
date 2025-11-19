# src/routes/babies.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src import models, schemas

router = APIRouter(prefix="/babies", tags=["Babies"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.BabyResponse)
def create_baby(baby: schemas.BabyCreate, db: Session = Depends(get_db)):
    new = models.Baby(name=baby.name, birth_date=baby.birth_date, gender=baby.gender)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.get("/", response_model=list[schemas.BabyResponse])
def list_babies(db: Session = Depends(get_db)):
    return db.query(models.Baby).all()


@router.get("/{baby_id}", response_model=schemas.BabyResponse)
def get_baby(baby_id: int, db: Session = Depends(get_db)):
    baby = db.query(models.Baby).filter(models.Baby.id == baby_id).first()
    if not baby:
        raise HTTPException(status_code=404, detail="Baby not found")
    return baby 
