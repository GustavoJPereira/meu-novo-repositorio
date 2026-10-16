from app.controller.erros import NaoEncontrado
from app.repository.pessoa_repository import pessoa_repository


class LoginController:
    def login(self, nome):
        try:
            return pessoa_repository.getByNome(nome)
        except KeyError:
            raise NaoEncontrado("Pessoa não encontrada")
