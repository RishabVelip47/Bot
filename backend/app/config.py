import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env", override=True)


APP_NAME = os.getenv(
    "APP_NAME",
    "AI Trading Platform"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)

DEBUG = os.getenv(
    "DEBUG",
    "true"
).lower() == "true"

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)