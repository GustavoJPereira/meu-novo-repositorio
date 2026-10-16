from app.controller.erros import Conflito, NaoEncontrado, Proibido
from app.model.emprestimo import Emprestimo
from app.model.livro import Livro
from app.repository.emprestimo_repository import emprestimo_repository
from app.repository.livro_repository import livro_repository
from app.repository.pessoa_repository import pessoa_repository


class LivroController:
    def getAll(self):
        return livro_repository.getAllLivro()

    def getById(self, id):
        try:
            return livro_repository.getLivro(id)
        except KeyError:
            raise NaoEncontrado("Nenhum livro encontrado")

    def getDisponiveis(self):
        return livro_repository.getDisponiveis()

    def cadastrar(self, pessoa_id, nome, ano_publicacao):
        try:
            pessoa = pessoa_repository.getPessoa(pessoa_id)
        except KeyError:
            raise NaoEncontrado("Pessoa não encontrada")
        if not pessoa.tem_permissao("cadastrar_livro"):
            raise Proibido("Sem permissão para cadastrar livro")
        try:
            livro = Livro(None, nome, ano_publicacao)
        except ValueError as e:
            raise Conflito(str(e))
        return livro_repository.addLivro(livro)

    def emprestar(self, livro_id, pessoa_id):
        livro = self.getById(livro_id)
        try:
            pessoa = pessoa_repository.getPessoa(pessoa_id)
        except KeyError:
            raise NaoEncontrado("Pessoa não encontrada")
        if livro.is_emprestado():
            raise Conflito("Livro já está emprestado")
        if len(emprestimo_repository.getByPessoa(pessoa.id)) >= pessoa.MAX_EMPRESTIMOS:
            raise Conflito(f"Limite de {pessoa.MAX_EMPRESTIMOS} empréstimos atingido")
        livro.emprestar_para(pessoa)
        livro_repository.attLivro(livro.id, livro)
        return emprestimo_repository.addEmprestimo(Emprestimo(livro, pessoa))
