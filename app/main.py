from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="API de Alunos")

alunos_db = [
    {"id": 1, "nome": "Leandro Souza", "email": "leandro@exemplo.com"}
]

class Aluno(BaseModel):
    id: int
    nome: str
    email: EmailStr


@app.get("/alunos")
def listar_alunos():
    return alunos_db


@app.get("/alunos/{aluno_id}")
def buscar_aluno(aluno_id: int):
    for aluno in alunos_db:
        if aluno["id"] == aluno_id:
            return aluno
    raise HTTPException(status_code=404, detail="Aluno não encontrado")


@app.post("/alunos", status_code=201)
def criar_aluno(aluno: Aluno):
    for a in alunos_db:
        if a["id"] == aluno.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    alunos_db.append(aluno.model_dump())
    return aluno
