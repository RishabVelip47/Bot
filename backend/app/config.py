import os
from dotenv import load_dotenv

load_dotenv()


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