from app.model.livro import Livro
#from app.repository.livro_repository import livro_repository

class LivroController: 
    def __init__(self):
        pass

    def getAll(self):
        pass
    #    return livro_repository.getAll()

    def getById(self, id):
    #    return livro_repository.getLivro(id)
        pass

    def getDisponiveis(self):
    #    return livro_repository.getDisponiveis()
        pass
    def emprestar(livro, leitor):
        livro.emprestar_para(leitor)
    #    livro_repository.attLivro(livro.id, livro)