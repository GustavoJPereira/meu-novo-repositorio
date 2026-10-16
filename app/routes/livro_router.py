from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.controller.erros import Conflito, NaoEncontrado, Proibido
from app.controller.livro_controller import LivroController

router = APIRouter(prefix="/api/livros", tags=["livros"])
emprestimos_router = APIRouter(prefix="/api/emprestimos", tags=["emprestimos"])
controller = LivroController()


class EmprestimoIn(BaseModel):
    livro_id: int
    pessoa_id: int


class LivroIn(BaseModel):
    pessoa_id: int
    nome: str
    ano_publicacao: int


@router.get("")
def getAll():
    return [l.to_dict() for l in controller.getAll()]


@router.get("/disponiveis")
def getDisponiveis():
    return [l.to_dict() for l in controller.getDisponiveis()]


@router.get("/{id}")
def getById(id: int):
    try:
        return controller.getById(id).to_dict()
    except NaoEncontrado as e:
        raise HTTPException(404, str(e))


@router.post("", status_code=201)
def cadastrar(body: LivroIn):
    try:
        return controller.cadastrar(body.pessoa_id, body.nome, body.ano_publicacao).to_dict()
    except NaoEncontrado as e:
        raise HTTPException(404, str(e))
    except Proibido as e:
        raise HTTPException(403, str(e))
    except Conflito as e:
        raise HTTPException(409, str(e))


@emprestimos_router.post("", status_code=201)
def emprestar(body: EmprestimoIn):
    try:
        return controller.emprestar(body.livro_id, body.pessoa_id).to_dict()
    except NaoEncontrado as e:
        raise HTTPException(404, str(e))
    except Conflito as e:
        raise HTTPException(409, str(e))
