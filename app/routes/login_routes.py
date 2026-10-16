from fastapi import APIRouter, HTTPException
## import do controller de login faltando

router = APIRouter(prefix="/api/login", tags=["login"])
## faltando instancia controller

@router.post("", status_code=201)
def criarUsuario(Leitor: leitor):
    ## criar usuario
    pass