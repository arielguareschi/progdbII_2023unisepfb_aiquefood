from fastapi import APIRouter

from api.v1.endpoints import (
    categoria,
    usuario
)

api_router = APIRouter()
api_router.include_router(
    categoria.router, prefix='/categorias', tags=['Categorias'])

api_router.include_router(
    usuario.router, prefix='/usuarios', tags=['Usuarios'])
