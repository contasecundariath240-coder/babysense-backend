from fastapi import FastAPI
from routers.babies import router as babies_router
from routers.measurements import router as measurements_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend online"}

app.include_router(babies_router, prefix="/babies")
app.include_router(measurements_router, prefix="/measurements") 
