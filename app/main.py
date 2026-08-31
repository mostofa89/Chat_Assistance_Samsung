from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database.connection import engine, Base, get_db
from .database import models
from .database.crud import get_all_phones, get_phone

from .chatbot import answer_question
from .rag.retriever import build_index
from .database.connection import SessionLocal  # or however you get a session
from .agents.crew import PhoneReviewCrew
from .chatbot.comparison import compare_phones

db = SessionLocal()
phones = get_all_phones(db)
phone_index = build_index(phones)
db.close()

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
    answer = answer_question(phone_index, request.question)
    return {"question": request.question, "answer": answer}


@app.get("/phones/{phone_name}/review")
def phone_review(phone_name: str, db: Session = Depends(get_db)):
    phone = get_phone(db, phone_name)
    if not phone:
        raise HTTPException(status_code=404, detail="Phone not found")
    crew = PhoneReviewCrew(db)
    return crew.run(phone)

@app.get("/compare")
def compare(phone1: str, phone2: str, db: Session = Depends(get_db)):
    p1, p2 = get_phone(db, phone1), get_phone(db, phone2)
    if not p1 or not p2:
        raise HTTPException(status_code=404, detail="One or both phones not found")
    return compare_phones(p1, p2)