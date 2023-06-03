from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    '''
    Configuracoes Gerais da API
    '''
    API_V1_STR: str = '/api/v1'
    # DB_URL: str = 'postgresql+asyncpg://usuario:senha@localhost:5432/aiquefood'
    DB_URL: str = 'mysql+aiomysql://aiquefood:1234567890@localhost:3306/aiquefood'
    DBBaseModel = declarative_base()

    '''
    import secrets
    token: str = secrets.token_urlsafe(32)
    print(token)
    '''
    
    JWT_SECRET: str = 'r1QdzNvWye8GjMv4vvqgM-DufjKxS3DcPnSnhEWXlr4'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTS: int = 7 * 24 * 60
    
    class Config:
        case_sensitive = True


settings = Settings()
