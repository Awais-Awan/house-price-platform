from fastapi import FastAPI
from app.core.config import settings

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