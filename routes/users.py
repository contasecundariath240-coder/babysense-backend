from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserLogin, UserResponse
from utils.hash import hash_password, verify_password
from utils.jwt import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])

# Criar usuário
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    hashed = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Login
@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()

    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token, "token_type": "bearer"}


# Buscar usuário atual
@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)):
    return current_user


# Atualizar usuário
@router.put("/update", response_model=UserResponse)
def update_user(
    updated: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    current_user.name = updated.name
    current_user.email = updated.email

    if updated.password:
        current_user.password = hash_password(updated.password)

    db.commit()
    db.refresh(current_user)

    return current_user


# Deletar usuário
@router.delete("/delete")
def delete_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db.delete(current_user)
    db.commit()
    return {"detail": "Usuário deletado com sucesso"} 
