import os
from typing import Optional, ClassVar
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from dotenv import load_dotenv

if not os.getenv("DATABASE_URL"):
    load_dotenv()


class Settings(BaseSettings):
    model_config = ConfigDict(case_sensitive=True)

    PROJECT_NAME: str = "Demo App"
    APP_ENV: str = os.environ['APP_ENV']

    # Base URL
