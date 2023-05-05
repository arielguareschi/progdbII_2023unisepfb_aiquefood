from core.configs import settings

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class CategoriaModel(settings.DBBaseModel):
    __tablename__ = 'categorias'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    descricao: str = Column(String(100))
    icone: str = Column(String(200))
    eh_ativa: bool = Column(Boolean)
    produtos = relationship(
        "CategoriaModel", cascade="all, delete-orphan",
        back_populates='categoria',
        uselist=True,
        lazy="joined"
    )
