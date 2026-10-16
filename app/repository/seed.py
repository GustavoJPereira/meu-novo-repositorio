from app.model.bibliotecario import Bibliotecario
from app.model.leitor import Leitor
from app.model.livro import Livro
from app.repository.livro_repository import livro_repository
from app.repository.pessoa_repository import pessoa_repository


def popular():
    pessoa_repository.addPessoa(Leitor(None, "Ana"))
    pessoa_repository.addPessoa(Bibliotecario(None, "Beto"))
    livro_repository.addLivro(Livro(None, "Dom Casmurro", 1899))
    livro_repository.addLivro(Livro(None, "Capitães da Areia", 1937))
    livro_repository.addLivro(Livro(None, "O Cortiço", 1890))
    livro_repository.addLivro(Livro(None, "Vidas Secas", 1938))
    livro_repository.addLivro(Livro(None, "Memórias Póstumas de Brás Cubas", 1881))
