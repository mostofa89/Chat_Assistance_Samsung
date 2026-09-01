from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database.connection import engine, Base, get_db, SessionLocal
from .database.crud import get_all_phones, get_phone

from .chatbot import answer_question
from .rag.retriever import build_index
from .agents.crew import PhoneReviewCrew
from .chatbot.comparison import compare_phones


# ============================================================
# DATABASE
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# BUILD PHONE VECTOR INDEX
# ============================================================

phone_index = None

db = SessionLocal()

try:
    phone_records = get_all_phones(db)

    if phone_records:
        phone_index = build_index(phone_records)

        print(f"Documents: {len(phone_records)}")
        print(f"Vector dimension: {phone_index.d}")

    else:
        print("No phone records found in database.")

finally:
    db.close()


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Samsung Phone AI Assistant",
    description="AI assistant for Samsung smartphone specifications",
    version="1.0.0"
)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Samsung Phone AI Assistant is running"
    }


# ============================================================
# GET ALL PHONES
# ============================================================

@app.get("/phones")
def get_phones(
    db: Session = Depends(get_db)
):
    results = get_all_phones(db)

    return [
        {
            "id": phone.id,
            "name": phone.name,

            "release_date": phone.release_date,
            "status": phone.status,
            "source_url": phone.source_url,

            "technology": phone.technology,
            "speed": phone.speed,

            "dimensions": phone.dimensions,
            "weight": phone.weight,
            "build": phone.build,
            "sim": phone.sim,
            "ip_rating": phone.ip_rating,

            "display_type": phone.display_type,
            "display_size": phone.display_size,
            "display_resolution": phone.display_resolution,
            "display_protection": phone.display_protection,
            "display_refresh_rate": phone.display_refresh_rate,
            "display_brightness": phone.display_brightness,

            "os": phone.os,
            "chipset": phone.chipset,
            "cpu": phone.cpu,
            "gpu": phone.gpu,

            "ram": phone.ram,
            "storage": phone.storage,
            "card_slot": phone.card_slot,

            "main_camera": phone.main_camera,
            "ultrawide_camera": phone.ultrawide_camera,
            "telephoto_camera": phone.telephoto_camera,
            "depth_camera": phone.depth_camera,

            "main_camera_features": phone.main_camera_features,
            "main_camera_video": phone.main_camera_video,

            "selfie_camera": phone.selfie_camera,
            "selfie_video": phone.selfie_video,

            "loudspeaker": phone.loudspeaker,
            "headphone_jack": phone.headphone_jack,

            "wlan": phone.wlan,
            "bluetooth": phone.bluetooth,
            "gps": phone.gps,
            "nfc": phone.nfc,
            "radio": phone.radio,
            "usb": phone.usb,

            "sensors": phone.sensors,

            "battery": phone.battery,
            "charging": phone.charging,
            "wireless_charging": phone.wireless_charging,

            "colors": phone.colors,
            "price": phone.price,
            "models": phone.models
        }
        for phone in results
    ]


# ============================================================
# CHAT REQUEST MODEL
# ============================================================

class ChatRequest(BaseModel):
    question: str


# ============================================================
# CHAT ENDPOINT
# ============================================================

@app.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    try:
        phones = get_all_phones(db)

        answer = answer_question(
            phone_index,
            request.question,
            phones
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:
        print("CHAT ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# PHONE REVIEW
# ============================================================

@app.get("/phones/{phone_name}/review")
def phone_review(
    phone_name: str,
    db: Session = Depends(get_db)
):
    phone = get_phone(db, phone_name)

    if not phone:
        raise HTTPException(
            status_code=404,
            detail="Phone not found"
        )

    try:
        crew = PhoneReviewCrew(db)

        result = crew.run(phone)

        return {
            "phone": phone.name,
            "specifications": result["specifications"],
            "review": result["review"],
            "overall_score": result["overall_score"],
            "category_scores": result["category_scores"]
        }

    except Exception as e:
        print("REVIEW ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=f"Review generation failed: {str(e)}"
        )

# ============================================================
# PHONE COMPARISON
# ============================================================

@app.get("/compare")
def compare(
    phone1: str,
    phone2: str,
    db: Session = Depends(get_db)
):

    p1 = get_phone(
        db,
        phone1
    )

    p2 = get_phone(
        db,
        phone2
    )

    if not p1:
        raise HTTPException(
            status_code=404,
            detail=f"Phone not found: {phone1}"
        )

    if not p2:
        raise HTTPException(
            status_code=404,
            detail=f"Phone not found: {phone2}"
        )

    try:
        result = compare_phones(
            p1,
            p2
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
