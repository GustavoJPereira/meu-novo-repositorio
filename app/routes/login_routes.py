from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.controller.erros import NaoEncontrado
from app.controller.login_controller import LoginController

router = APIRouter(prefix="/api/login", tags=["login"])
controller = LoginController()


class LoginIn(BaseModel):
    nome: str


@router.post("")
def login(body: LoginIn):
    try:
        return controller.login(body.nome).to_dict()
    except NaoEncontrado as e:
        raise HTTPException(404, str(e))
