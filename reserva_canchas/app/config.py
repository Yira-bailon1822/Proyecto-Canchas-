from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # Ignora las variables del .env que no estén declaradas aquí
    )

settings = Settings()