from fastapi import APIRouter, HTTPException
from app.controller.leitor_controller import LeitorController

router = APIRouter(prefix="/api/pessoas", tags=["pessoas", "leitores"])
controller = LeitorController()

@router.get("/{idUser}/emprestimos")
def emprestimos(idUser):
    return controller.listar_emprestimos(idUser)

