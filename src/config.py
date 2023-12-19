from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    service_name: str = "Character Generator"
    k_revision: str = "Local"
    log_level: str = "DEBUG"
    openai_key: str = os.getenv("OPENAI_KEY")
    model: str = "gpt_3_5_turbo"
    google_vision_api = os.getenv("PATH_TO_KEY")

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
