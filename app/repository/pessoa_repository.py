from app.repository.in_memory_table import InMemoryTable


class PessoaRepository:
    def __init__(self):
        self.table = InMemoryTable()

    def addPessoa(self, pessoa):
        return self.table.newRegistro(pessoa)

    def getPessoa(self, id):
        return self.table.getRegistro(id)

    def getByNome(self, nome):
        for pessoa in self.table.getAll():
            if pessoa.nome.lower() == nome.lower():
                return pessoa
        raise KeyError("pessoa nao encontrada")


pessoa_repository = PessoaRepository()
