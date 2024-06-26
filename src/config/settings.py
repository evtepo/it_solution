from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    project_name: str = Field(alias="PROJECT_NAME", default="IT-Solutions")

    localhost: str = Field(alias="LOCALHOST", default="localhost")
    localport: int = Field(alias="LOCALPORT", default=8000)

    postgres_db: str = Field(alias="POSTGRES_DB", default="advertisement")
    postgres_user: str = Field(alias="POSTGRES_USER", default="postgres")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD", default="postgres")
    postgres_host: str = Field(alias="POSTGRES_HOST", default="localhost")
    postgres_port: str = Field(alias="POSTGRES_PORT", default="5432")


settings = Settings()

dsn = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
