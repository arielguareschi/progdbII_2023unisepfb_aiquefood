from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.future import select
from core.deps import get_session

from sqlalchemy.ext.asyncio import AsyncSession
from models.categoria_model import CategoriaModel

from schemas.categoria_schema import CategoriaSchema


router = APIRouter()


@router.get('/', response_model=List[CategoriaSchema])
async def get_categorias(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel)
        result = await session.execute(query)
        categorias: List[CategoriaModel] = result.scalars().all()

        return categorias


@router.get('/{categoria_id}', response_model=CategoriaSchema, status_code=status.HTTP_200_OK)
async def get_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(
            CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria = result.scalar_one_or_none()
        if categoria:
            return categoria
        else:
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CategoriaSchema)
async def post_categoria(categoria: CategoriaSchema, db: AsyncSession = Depends(get_session)):
    novo_categoria = CategoriaModel(descricao=categoria.descricao,
                                    icone=categoria.icone,
                                    eh_ativa=categoria.eh_ativa)
    db.add(novo_categoria)
    await db.commit()

    return novo_categoria


@router.put('/{categoria_id}', response_model=CategoriaSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_categoria(categoria_id: int, categoria: CategoriaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(
            CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria_up = result.scalar_one_or_none()

        if categoria_up:
            categoria_up.descricao = categoria.descricao
            categoria_up.icone = categoria.icone
            categoria_up.eh_ativa = categoria.eh_ativa
            await session.commit()

            return categoria_up
        else:
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{categoria_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(
            CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria_del = result.scalar_one_or_none()

        if categoria_del:
            await session.delete(categoria_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)
