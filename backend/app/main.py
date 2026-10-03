from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import APP_NAME, APP_ENV, DEBUG
from app.logger import setup_logger


logger = setup_logger()


app = FastAPI(
    title=APP_NAME,
    description="Backend API for the AI Multi-Asset Trading Platform",
    version="0.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():

    logger.info("Root endpoint accessed")

    return {
        "message": "AI Trading Platform API is running",
        "environment": APP_ENV,
        "debug": DEBUG
    }


@app.get("/health")
def health_check():

    logger.info("Health check requested")

    return {
        "status": "healthy"
    }