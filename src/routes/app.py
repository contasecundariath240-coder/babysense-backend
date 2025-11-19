from fastapi import FastAPI
from routes.measurements import measurements_bp
from routes.babies import babies_bp

app = FastAPI()

app.include_router(measurements_bp)
app.include_router(babies_bp)
