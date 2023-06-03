from core.configs import settings

from sqlalchemy import Column, Integer, String, Boolean


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=True)
    sobrenome = Column(String(100), nullable=True)
    email = Column(String(200), index=True, nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    eh_admin = Column(Boolean, default=False)
