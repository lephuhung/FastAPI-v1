from functools import lru_cache
from typing import Any, Dict, Optional, Union

from pydantic import PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",case_sensitive=True)

    PROJECT_NAME: str = "FastAPI Role Based Access Control Auth Service"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    USERS_OPEN_REGISTRATION: str
    ENVIRONMENT: Optional[str]
    PORT: Optional[int]
    FIRST_SUPER_ADMIN_EMAIL: str
    FIRST_SUPER_ADMIN_PASSWORD: str
    FIRST_SUPER_ADMIN_ACCOUNT_NAME: str
    ALGORITHM : str
    POSTGRES_SERVER: Optional[str] 
    POSTGRES_USER: Optional[str] 
    POSTGRES_PASSWORD: Optional[str] 
    POSTGRES_DB: Optional[str] 

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_POSTGRES_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str):
            print("Loading SQLALCHEMY_DATABASE_URI from .docker.env file ...")
            return v
        print("Creating SQLALCHEMY_DATABASE_URI from .env file ...")
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        )          


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
