from app.repository.in_memory_table import InMemoryTable


class LivroRepository:
    def __init__(self):
        self.table = InMemoryTable()

    def addLivro(self, livro):
        return self.table.newRegistro(livro)

    def getLivro(self, id):
        return self.table.getRegistro(id)

    def attLivro(self, id, livro):
        return self.table.attRegistro(id, livro)

    def getAllLivro(self):
        return self.table.getAll()

    def getDisponiveis(self):
        return [reg for reg in self.table.getAll() if not reg.is_emprestado()]


livro_repository = LivroRepository()
