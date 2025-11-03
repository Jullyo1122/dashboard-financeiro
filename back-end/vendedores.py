from fastapi import FastAPI, HTTPException
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

vendedores_db = {
    1: {
        "nome": "Carlos Almeida",
        "email": "carlos@empresa.com",
        "cargo": "Vendedor",
        "meta_mensal": 10000.0,
        "vendas_realizadas": 5,
        "total_vendido": 3500.0,
        "status": "Ativo"
    },
    2: {
        "nome": "Maria Souza",
        "email": "maria@empresa.com",
        "cargo": "Supervisora",
        "meta_mensal": 20000.0,
        "vendas_realizadas": 10,
        "total_vendido": 18000.0,
        "status": "Ativo"
    }
}

@app.post('/DadosVendedores')
def acao_adicionar(dados: DadosVendedores):
    if dados.email in vendedores_db:
        return {"status": "Erro", "mensagem": "Esse email já está cadastrado"}
    return {"status": "sucesso", "mensagem": "Vendedor adicionado com sucesso"}


@app.put('/DadosVendedores/{vendedor_id}')
def acao_editar(vendedor_id: int, dados: DadosVendedores):

    if vendedor_id not in vendedores_db:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
      
    vendedores_db[vendedor_id] = dados.dict()
    
    return {"mensagem": "Dados do vendedor atualizados com sucesso!", "vendedor": vendedores_db[vendedor_id]}

@app.delete('/DadosVendedores/{vendedor_id}')
def acao_deletar(vendedor_id: int):

    if vendedor_id not in vendedores_db:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")

    vendedor_removido = vendedores_db.pop(vendedor_id)
    return {"mensagem": "Vendedor removido com sucesso!", "vendedor": vendedor_removido}