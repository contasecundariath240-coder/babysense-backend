from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import router as auth_router
from babies import router as babies_router
from measurements import router as measurements_router

app = FastAPI(
    title="BabySense API",
    description="Backend oficial do aplicativo BabySense",
    version="1.0.0"
)

# CORS – libera o app para funcionar no celular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(babies_router, prefix="/babies", tags=["Babies"])
app.include_router(measurements_router, prefix="/measurements", tags=["Measurements"])

@app.get("/")
def home():
    return {"status": "BabySense API funcionando!"} 
