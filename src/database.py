# src/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Busca a URL do banco (Render ou local)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

# Converte automaticamente para o driver correto
if DATABASE_URL.startswith("postgres://") or DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://")
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://")

# Cria a engine e sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
