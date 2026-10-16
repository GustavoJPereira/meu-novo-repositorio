from app.model.pessoa import Pessoa


class Bibliotecario(Pessoa):
    MAX_EMPRESTIMOS = 10
    PERMISSOES = ["cadastrar_livro"]

    def get_tipo(self):
        return "bibliotecário"
