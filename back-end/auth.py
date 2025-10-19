from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    email: str
    senha: str

class Cadastrar(BaseModel):
    nome: str
    cpf: str
    email: str
    senha: str

db = {
    1: {"nome": "Lucas Santos","cpf": "123.456.789-10", "email": "luquinhas99@gmail.com", "senha": "Klark25"},
    2: {"nome": "João Gustavo de Souza", "cpf": "111.213.141-15", "email": "joaokaik@gmail.com", "senha": "famosinho123"},
    3: {"nome": "Augusto Soares dos Santos ", "cpf": "161.718.192-20", "email": "agostinho@gmail.com", "senha": "arrascapeta123"}
}

@app.post('/Login')
def login(dados: Login):
    for user in db.values():
        if user["email"] == dados.email and user["senha"] == dados.senha:
            return {
                "status": "sucesso",
                "mensagem": "Login realizado!",
                }
    return {"status": "erro", "mensagem": "Usuário ou senha incorretos"}

@app.post('/Cadastrar')
def cadastro(dados: Cadastrar):
    for user in db.values():
        if user["cpf"] == dados.cpf:
            return {"status": "erro", "mensagem": "CPF já cadastrado."}
        if user["email"] == dados.email:
            return {"status": "erro", "mensagem": "E-mail já cadastrado."}
    return {"status": "sucesso", "mensagem": "Cadastro realizado com sucesso!"}