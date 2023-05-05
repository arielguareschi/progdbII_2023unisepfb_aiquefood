from typing import List, Optional
from pydantic import BaseModel

from schemas.produto_schema import ProdutoSchema


class CategoriaSchema(BaseModel):
    id: Optional[int]
    descricao: str
    icone: str
    eh_ativa: bool

    class Config:
        orm_mode = True

class CategoriaSchemaProdutos(CategoriaSchema):
    produtos: Optional[List[ProdutoSchema]]
    