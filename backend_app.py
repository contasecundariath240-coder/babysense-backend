from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.users import router as users_router
from routers.babies import router as babies_router
from routers.measurements import router as measurements_router 

app = FastAPI(title="BabySense API")

# Libera acesso do seu app mobile
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "BabySense API funcionando!"}

# Inclui as rotas
app.include_router(users_router, prefix="/users", tags=["Usuários"])
app.include_router(babies_router, prefix="/babies", tags=["Bebês"])
app.include_router(measurements_router, prefix="/measurements", tags=["Medições"]) 
