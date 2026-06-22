from fastapi import FastAPI

from secao03_p2.routes import curso_router
from secao03_p2.routes import usuario_router

app = FastAPI()
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuario'])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("secao03_p2.main:app", host="0.0.0.0", port=8000, reload=True)