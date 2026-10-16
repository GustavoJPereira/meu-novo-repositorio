# Tema 1 — Biblioteca comunitária
Controle de acervo e empréstimos de um ponto de leitura de bairro.


## Camada 
- Entidades
- Hierarquia
- Liga as duas


## O que criar
- Livro, Emprestimo
- Pessoa → Leitor → Bibliotecario
- Emprestimo guarda um Livro e uma Pessoa

## Regras obrigatórias
- Leitor pode ter no máximo 3 empréstimos; bibliotecário, 10 (constante de classe)
- Não é possível emprestar um livro já emprestado
- O ano de publicação não pode ser maior que o ano atual
- Só quem tem a permissão cadastrar_livro pode incluir um título novo

## Rotas mínimas
- GET /api/livros lista o acervo
- GET /api/livros/{id} um livro, ou 404
- GET /api/livros/disponiveis só os que não estão emprestados
- POST /api/emprestimos registra, 201 ou 409
- GET /api/pessoas/{id}/emprestimos o que a pessoa está com
- POST /api/login perfil e permissões

### Rotas extras necessárias


## TO-DO
[] criar rotas com mocks
[] substituir mocks por mongo db pq tenho preguiça
[] subir num container na ps para apresentação

## Schema

Livro: id | nome | emprestado_para(Usuario)
Usuario: id | tipo("leitor"|"bibliotecário") | nome

