from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Project settings
    PROJECT_NAME: str = "FastAPI Starter Kit"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A modern FastAPI starter kit with best practices"

    # API settings
    API_V1_PREFIX: str = "/api/v1"

    # CORS settings
    CORS_ORIGINS: list[str] = ["*"]

    # Database settings
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "fastapi_starter"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


def get_settings() -> Settings:
    return Settings()
