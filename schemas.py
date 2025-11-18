from pydantic import BaseModel, EmailStr
from typing import Optional

# Criar usuário
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Resposta do usuário
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True 
# -----------------------------
# BEBÊS
# -----------------------------

class BabyBase(BaseModel):
    name: str
    gender: str
    birth_date: str  # YYYY-MM-DD

class BabyCreate(BabyBase):
    pass

class BabyUpdate(BaseModel):
    name: str | None = None
    gender: str | None = None
    birth_date: str | None = None

class BabyResponse(BabyBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True 
