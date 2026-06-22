from typing import Any, ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:1234@localhost:5432/faculdade"
    DBBaseModel: ClassVar[Any] = declarative_base()

    class Config:
        case_sensitive = True

settings =  Settings()