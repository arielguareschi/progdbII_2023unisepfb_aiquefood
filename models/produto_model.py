from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import relationship
from core.configs import Settings


class ProdutoModel(Settings.DBBaseModel):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(Text)
    preco = Column(Numeric(15, 2))
    fracionado = Column(Boolean, default=False)
    avaliacao = Column(SmallInteger, default=5)
    tamanho = Column(String(5))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship("CategoriaModel", back_populates='produtos', lazy='joined')
