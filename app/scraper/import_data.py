from app.database.connection import SessionLocal
from app.database.crud import create_phone


phones = [

    {
        "name": "Samsung Galaxy S21",
        "display": "6.2 inch",
        "chipset": "Example chipset",
        "battery": "4000 mAh",
        "main_camera": "12 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S22",
        "display": "6.1 inch",
        "chipset": "Example chipset",
        "battery": "3700 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S23",
        "display": "6.1 inch",
        "chipset": "Example chipset",
        "battery": "3900 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    }
]


db = SessionLocal()


for phone in phones:

    create_phone(
        db,
        phone
    )


db.close()

print("Data inserted successfully.")