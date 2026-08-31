from fastapi import FastAPI

from .database.connection import engine, Base
from .database import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Samsung Phone AI Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Samsung Phone AI Assistant is running"
    }