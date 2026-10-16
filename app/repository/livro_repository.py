class LivroRepository:
    def __init__(self):
        if hasattr("_inicializado"):
            return
        _inicializado = True
        self.table = self.InMemoryTable()

    def addLivro(self, livro):
        return self.table.newRegistro(livro)
    
    def getLivro(self, id):
        return self.table.getRegistro(id)

    def attLivro(self, id, livro):
        return self.table.attRegistro(id, livro)

    def getAllLivro(self):
        return self.table.getAll()

    def getDisponiveis(self):
        return [reg for reg in self.table.getAll() if not reg.emprestar_para]
