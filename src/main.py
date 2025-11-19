# src/main.py
from fastapi import FastAPI
from src.database import engine, Base
from src.routes.babies import router as babies_router
from src.routes.measurements import router as measurements_router

# Create tables (if not created). You can remove this after you add migrations.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BabySense Backend")

app.include_router(babies_router)
app.include_router(measurements_router)


@app.get("/")
def root():
    return {"message": "Backend is running!"} 
