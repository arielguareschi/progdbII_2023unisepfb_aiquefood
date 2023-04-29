from typing import Optional
from pydantic import BaseModel


class CategoriaSchema(BaseModel):
    id: Optional[int]
    descricao: str
    icone: str
    eh_ativa: bool

    class Config:
        orm_mode = True
