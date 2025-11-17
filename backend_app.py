from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados para receber temperatura
class TemperatureData(BaseModel):
    baby_id: str
    temperature: float

@app.get("/")
def home():
    return {"status": "BabySense API funcionando!"}

@app.post("/temperature")
def receive_temperature(data: TemperatureData):
    # Aqui futuramente você pode salvar no banco
    print(f"Temperatura recebida do bebê {data.baby_id}: {data.temperature}")
    
    return {
        "message": "Temperatura recebida com sucesso!",
        "dados": data
    }
