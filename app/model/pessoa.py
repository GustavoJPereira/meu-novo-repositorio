class Pessoa:
    MAX_EMPRESTIMOS = 0
    PERMISSOES = []

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        raise NotImplementedError

    def tem_permissao(self, permissao):
        return permissao in self.PERMISSOES

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.get_tipo(),
            "permissoes": list(self.PERMISSOES),
        }
