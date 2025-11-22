from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Text Similarity API"
    HF_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
