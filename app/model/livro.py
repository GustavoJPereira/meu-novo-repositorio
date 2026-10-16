from datetime import date


class Livro:
    def __init__(self, id, nome, ano_publicacao, usuario=None):
        if ano_publicacao > date.today().year:
            raise ValueError("O ano de publicação não pode ser maior que o ano atual")
        self.id = id
        self.nome = nome
        self.ano_publicacao = ano_publicacao
        self.emprestado_para = None
        if usuario:
            self.emprestar_para(usuario)

    def emprestar_para(self, usuario):
        self.emprestado_para = usuario

    def is_emprestado(self):
        return self.emprestado_para is not None

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_mutuario(self):
        return self.emprestado_para

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ano_publicacao": self.ano_publicacao,
            "emprestado_para": self.emprestado_para.to_dict() if self.emprestado_para else None,
        }
