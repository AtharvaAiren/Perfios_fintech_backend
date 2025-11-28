import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@db:5432/agrisure")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretjwtkey")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    S3_BUCKET: str = os.getenv("S3_BUCKET", "")

    PERFIOS_API_URL: str = os.getenv("PERFIOS_API_URL", "")
    PERFIOS_API_KEY: str = os.getenv("PERFIOS_API_KEY", "")

    ONEVIGIL_API_URL: str = os.getenv("ONEVIGIL_API_URL", "")
    ONEVIGIL_API_KEY: str = os.getenv("ONEVIGIL_API_KEY", "")

settings = Settings()
