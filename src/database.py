# src/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")  # fallback local sqlite for dev

# For PostgreSQL in Render, DATABASE_URL should be set in env vars (example: postgres://user:pass@host:port/dbname)
engine = create_engine(DATABASE_URL, future=True, echo=False, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
