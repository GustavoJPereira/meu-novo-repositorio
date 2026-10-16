class Emprestimo:
    def __init__(self, livro, pessoa):
        self.id = None
        self.livro = livro
        self.pessoa = pessoa

    def to_dict(self):
        return {
            "id": self.id,
            "livro": self.livro.to_dict(),
            "pessoa": self.pessoa.to_dict(),
        }
