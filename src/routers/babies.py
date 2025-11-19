from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src import models
from src.schemas import BabyCreate, BabyResponse

router = APIRouter(prefix="/babies", tags=["Babies"])


@router.post("/", response_model=BabyResponse)
def create_baby(baby: BabyCreate, db: Session = Depends(get_db)):
    db_baby = models.Baby(**baby.dict())
    db.add(db_baby)
    db.commit()
    db.refresh(db_baby)
    return db_baby


@router.get("/", response_model=list[BabyResponse])
def list_babies(db: Session = Depends(get_db)):
    return db.query(models.Baby).all() 
