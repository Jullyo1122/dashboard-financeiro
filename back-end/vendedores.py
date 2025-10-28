from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DadosVendedores(BaseModel):
    nome: str
    email: str
    cargo: str
    meta_mensal: float
    vendas_realizadas: int
    total_vendido: float
    status: str

@app.put('/DadosVendedores')
def editar_vendedor(dados: DadosVendedores):
