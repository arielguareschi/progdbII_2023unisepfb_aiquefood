from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    '''
    Configuracoes Gerais da API
    '''
    API_V1_STR: str = '/api/v1'
    #DB_URL: str = 'postgresql+asyncpg://usuario:senha@localhost:5432/aiquefood'
    DB_URL: str = 'mysql+aiomysql://aiquefood:1234567890@localhost:3306/aiquefood'
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True
    
settings = Settings()
