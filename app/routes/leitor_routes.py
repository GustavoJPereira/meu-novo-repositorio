from fastapi import APIRouter, HTTPException

from app.controller.erros import NaoEncontrado
from app.controller.leitor_controller import LeitorController

router = APIRouter(prefix="/api/pessoas", tags=["pessoas", "leitores"])
controller = LeitorController()


@router.get("/{idUser}/emprestimos")
def emprestimos(idUser: int):
    try:
        return [e.to_dict() for e in controller.listar_emprestimos(idUser)]
    except NaoEncontrado as e:
        raise HTTPException(404, str(e))
