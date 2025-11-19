from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models import Baby
from src.schemas import BabyCreate, BabyResponse

router = APIRouter(prefix="/babies", tags=["Babies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BabyResponse)
def create_baby(baby: BabyCreate, db: Session = Depends(get_db)):
    db_baby = Baby(name=baby.name, birthdate=baby.birthdate)
    db.add(db_baby)
    db.commit()
    db.refresh(db_baby)
    return db_baby

@router.get("/", response_model=list[BabyResponse])
def list_babies(db: Session = Depends(get_db)):
    return db.query(Baby).all() 
