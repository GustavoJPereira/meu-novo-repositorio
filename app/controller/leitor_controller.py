from app.controller.erros import NaoEncontrado
from app.repository.emprestimo_repository import emprestimo_repository
from app.repository.pessoa_repository import pessoa_repository


class LeitorController:
    def listar_emprestimos(self, leitorId):
        try:
            pessoa_repository.getPessoa(leitorId)
        except KeyError:
            raise NaoEncontrado("Pessoa não encontrada")
        return emprestimo_repository.getByPessoa(leitorId)
