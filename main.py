from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.livro_router import router as livro_router, emprestimos_router
from app.repository.seed import popular
from app.routes.leitor_routes import router as leitor_router
from app.routes.login_routes import router as login_router 

app = FastAPI(title="Biblioteca", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)


popular()

app.include_router(livro_router)
app.include_router(emprestimos_router)
app.include_router(leitor_router)
app.include_router(login_router)

@app.get("/")
def raiz():
    return {"api": "Biblioteca", "docs": "/docs"}