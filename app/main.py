from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database.connection import engine, Base, get_db
from .database import models
from .database.crud import get_all_phones, get_phone

from .chatbot import answer_question


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


@app.get("/phones")
def phones(
    db: Session = Depends(get_db)
):

    results = get_all_phones(db)

    return [
        {
            "id": phone.id,
            "name": phone.name,
            "display": phone.display,
            "processor": phone.chipset,
            "battery": phone.battery
        }
        for phone in results
    ]


@app.get("/phones/{phone_name}")
def phone_details(
    phone_name: str,
    db: Session = Depends(get_db)
):

    phone = get_phone(
        db,
        phone_name
    )

    if not phone:

        raise HTTPException(
            status_code=404,
            detail="Phone not found"
        )

    return {
        "id": phone.id,
        "name": phone.name,
        "display": phone.display,
        "processor": phone.chipset,
        "ram": phone.ram,
        "storage": phone.storage,
        "main_camera": phone.main_camera,
        "ultrawide_camera": phone.ultrawide_camera,
        "telephoto_camera": phone.telephoto_camera,
        "selfie_camera": phone.selfie_camera,
        "video": phone.video,
        "battery": phone.battery,
        "charging": phone.charging,
        "operating_system": phone.operating_system,
        "weight": phone.weight,
        "price": phone.price,
        "source_url": phone.source_url
    }


class ChatRequest(BaseModel):

    question: str


@app.post("/chat")
def chat(request: ChatRequest):

    answer = answer_question(None, request.question)

    return {
        "question": request.question,
        "answer": answer
    }