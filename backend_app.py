from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para receber dados de temperatura
class TemperatureData(BaseModel):
    baby_id: str
    temperature: float

# Rota inicial
@app.get("/")
def home():
    return {"status": "BabySense API funcionando!"}

# Rota para receber temperatura
@app.post("/temperature")
def receive_temperature(data: TemperatureData):
    # Aqui futuramente vamos salvar no banco
    print(f"Temperatura recebida: {data.temperature} do bebê {data.baby_id}")

    # Resposta padrão
    return {
        "message": "Temperatura recebida com sucesso!",
        "data": data
    } 
