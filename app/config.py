from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    app_name: str

    class Config:
        env_file = ".env"

settings = Settings()
