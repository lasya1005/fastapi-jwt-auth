from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    JWT_SECRET: str
    JWT_EXPIRATION_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()
