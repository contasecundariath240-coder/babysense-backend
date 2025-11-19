rom fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src import models
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.BabyResponse)
def create_baby(baby: schemas.BabyCreate, db: Session = Depends(get_db)):
    new_baby = models.Baby(**baby.dict())
    db.add(new_baby)
    db.commit()
    db.refresh(new_baby)
    return new_baby


@router.get("/", response_model=list[schemas.BabyResponse])
def list_babies(db: Session = Depends(get_db)):
    return db.query(models.Baby).all() 
