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
