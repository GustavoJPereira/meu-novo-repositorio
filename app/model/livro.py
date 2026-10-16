class Livro: 
    def __init__(self, id, nome, usuario):
        self.id = id
        self.nome = nome
        emprestar_para(usuario) 

    def emprestar_para(self, usuario):
        self.emprestado_para = usuario
    
    def is_emprestado(self):
        if not self.emprestado_para:
            return True
        return False
    
    def get_id(self):
        return id
    
    def get_nome(self):
        return nome
    
    def get_mutuario(self):
        return self.emprestado_para