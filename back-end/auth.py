from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    email: str
    senha: str

db = {
    1: {"email": "luquinhas99@gmail.com", "senha": "Klark25"},
    2: {"email": "joaokaik@gmail.com", "senha": "famosinho123"},
    3: {"email": "agostinho@gmail.com", "senha": "arrascapeta123"}
}

@app.post('/Login')
def auth(dados: Login):
    if dados.email in db and db[dados.email]["senha"] == dados.senha:
         return {
            "status": "sucesso",
            "mensagem": "Login realizado!",
        }
    return {"status": "erro", "mensagem": "Usuário ou senha incorretos"}
