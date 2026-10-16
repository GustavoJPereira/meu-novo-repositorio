from app.repository.in_memory_table import InMemoryTable


class EmprestimoRepository:
    def __init__(self):
        self.table = InMemoryTable()

    def addEmprestimo(self, emprestimo):
        return self.table.newRegistro(emprestimo)

    def getByPessoa(self, pessoa_id):
        return [e for e in self.table.getAll() if e.pessoa.id == pessoa_id]


emprestimo_repository = EmprestimoRepository()
