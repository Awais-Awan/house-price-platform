from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)
logger.info("Starting the application...")

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
)


@app.get("/")
def root():
    return{
        "message" : f"Welcome to {settings.app_name} version {settings.version}!"
    }
    
@app.get("/health")
def health_check():
    return{
        "status" : "ok"
    }