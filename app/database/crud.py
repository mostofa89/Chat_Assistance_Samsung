from sqlalchemy.orm import Session

from .models import Phone


def create_phone(db: Session, phone_data: dict):

    # Check if phone already exists
    existing_phone = (
        db.query(Phone)
        .filter(Phone.name == phone_data["name"])
        .first()
    )

    if existing_phone:
        print(f"Already exists: {phone_data['name']}")
        return existing_phone

    # Create new phone
    phone = Phone(**phone_data)

    db.add(phone)
    db.commit()
    db.refresh(phone)

    print(f"Inserted: {phone_data['name']}")

    return phone


def get_all_phones(db: Session):

    return db.query(Phone).all()


def get_phone(db: Session, phone_name: str):

    return (
        db.query(Phone)
        .filter(Phone.name.ilike(phone_name))
        .first()
    )