from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    model_file: str


@lru_cache
def get_config() -> Config:
    return Config()