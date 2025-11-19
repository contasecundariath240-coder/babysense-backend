from fastapi import FastAPIfrom fastapi import FastAPI
from src.routers import babies, measurements
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(babies.router, prefix="/babies", tags=["Babies"])
app.include_router(measurements.router, prefix="/measurements", tags=["Measurements"])

@app.get("/")
def root():
    return {"message": "Backend is running!"} 
