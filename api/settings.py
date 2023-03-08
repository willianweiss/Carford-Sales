import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "Carford"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ALLOWED_HOSTS: list = os.getenv("ALLOWED_HOSTS", "").split(",")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")


settings = Settings()
