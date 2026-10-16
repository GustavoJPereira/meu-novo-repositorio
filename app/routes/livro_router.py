from fastapi import APIRouter, HTTPException
from app.controller.livro_controller import LivroController

router = APIRouter(prefix="/api/livros", tags=["livros"])
controller = LivroController()

@router.get("")
def getAll():
    return controller.getAll()

@router.get("/{id}")
def getById(id):
    livro = controller.getById(id)
    if not livro:
        raise HTTPException(404, "Nenhum livro encontrado")
    return livro

@router.get("/disponiveis")
def getDisponiveis():
    return controller.getDisponiveis()

@router.post("/emprestimos", status_code=201)
def emprestar(Livro: livro, Leitor: leitor):
    result = controller.emprestar(livro, leitor)
    if result.message:
        raise HTTPException(409, result.message)