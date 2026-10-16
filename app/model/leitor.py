from app.model.pessoa import Pessoa


class Leitor(Pessoa):
    MAX_EMPRESTIMOS = 3
    PERMISSOES = []

    def get_tipo(self):
        return "leitor"
