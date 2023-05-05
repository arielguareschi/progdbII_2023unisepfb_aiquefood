from typing import Optional
from pydantic import BaseModel


class ProdutoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str
    preco: float
    fracionado: bool
    avaliacao: int
    tamanho: str
    categoria_id: Optional[int]
    
    class Config:
        orm_mode = True
