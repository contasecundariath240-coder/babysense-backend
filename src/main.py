from fastapi import FastAPI
from src.database import Base, engine
from src.routers import babies, measurements

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rotas
app.include_router(babies.router, prefix="/babies", tags=["Babies"])
app.include_router(measurements.router, prefix="/measurements", tags=["Measurements"])

@app.get("/")
def root():
    return {"message": "Backend is running!"} 
