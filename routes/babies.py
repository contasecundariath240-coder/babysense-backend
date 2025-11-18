from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Baby, User
from schemas import BabyCreate, BabyResponse, BabyUpdate
from utils.jwt import get_current_user

router = APIRouter(prefix="/babies", tags=["Babies"])

# Criar bebê
@router.post("/", response_model=BabyResponse)
def create_baby(
    baby: BabyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_baby = Baby(
        name=baby.name,
        gender=baby.gender,
        birth_date=baby.birth_date,
        user_id=current_user.id
    )
    db.add(new_baby)
    db.commit()
    db.refresh(new_baby)
    return new_baby


# Listar bebês do usuário logado
@router.get("/", response_model=list[BabyResponse])
def list_babies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    babies = db.query(Baby).filter(Baby.user_id == current_user.id).all()
    return babies


# Buscar bebê específico
@router.get("/{baby_id}", response_model=BabyResponse)
def get_baby(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    baby = db.query(Baby).filter(
        Baby.id == baby_id,
        Baby.user_id == current_user.id
    ).first()

    if not baby:
        raise HTTPException(status_code=404, detail="Bebê não encontrado")

    return baby


# Atualizar bebê
@router.put("/{baby_id}", response_model=BabyResponse)
def update_baby(
    baby_id: int,
    update: BabyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    baby = db.query(Baby).filter(
        Baby.id == baby_id,
        Baby.user_id == current_user.id
    ).first()

    if not baby:
        raise HTTPException(status_code=404, detail="Bebê não encontrado")

    if update.name:
        baby.name = update.name
    if update.gender:
        baby.gender = update.gender
    if update.birth_date:
        baby.birth_date = update.birth_date

    db.commit()
    db.refresh(baby)
    return baby


# Deletar bebê
@router.delete("/{baby_id}")
def delete_baby(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    baby = db.query(Baby).filter(
        Baby.id == baby_id,
        Baby.user_id == current_user.id
    ).first()

    if not baby:
        raise HTTPException(status_code=404, detail="Bebê não encontrado")

    db.delete(baby)
    db.commit()
    return {"detail": "Bebê deletado com sucesso"} 
