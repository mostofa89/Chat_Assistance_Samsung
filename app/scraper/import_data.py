from app.database.connection import SessionLocal
from app.database.models import Phone


phones = [

    {
        "name": "Samsung Galaxy S21",
        "display": "6.2 inch",
        "chipset": "Exynos 2100 / Snapdragon 888",
        "ram": "8GB",
        "battery": "4000 mAh",
        "main_camera": "12 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S21+",
        "display": "6.7 inch",
        "chipset": "Exynos 2100 / Snapdragon 888",
        "ram": "8GB",
        "battery": "4800 mAh",
        "main_camera": "12 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S21 Ultra",
        "display": "6.8 inch",
        "chipset": "Exynos 2100 / Snapdragon 888",
        "ram": "12GB / 16GB",
        "battery": "5000 mAh",
        "main_camera": "108 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S22",
        "display": "6.1 inch",
        "chipset": "Exynos 2200 / Snapdragon 8 Gen 1",
        "ram": "8GB",
        "battery": "3700 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S22+",
        "display": "6.6 inch",
        "chipset": "Exynos 2200 / Snapdragon 8 Gen 1",
        "ram": "8GB",
        "battery": "4500 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S22 Ultra",
        "display": "6.8 inch",
        "chipset": "Exynos 2200 / Snapdragon 8 Gen 1",
        "ram": "8GB / 12GB",
        "battery": "5000 mAh",
        "main_camera": "108 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S23",
        "display": "6.1 inch",
        "chipset": "Snapdragon 8 Gen 2",
        "ram": "8GB",
        "battery": "3900 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S23+",
        "display": "6.6 inch",
        "chipset": "Snapdragon 8 Gen 2",
        "ram": "8GB",
        "battery": "4700 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S23 Ultra",
        "display": "6.8 inch",
        "chipset": "Snapdragon 8 Gen 2",
        "ram": "8GB / 12GB",
        "battery": "5000 mAh",
        "main_camera": "200 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S24",
        "display": "6.2 inch",
        "chipset": "Exynos 2400 / Snapdragon 8 Gen 3",
        "ram": "8GB",
        "battery": "4000 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S24+",
        "display": "6.7 inch",
        "chipset": "Exynos 2400 / Snapdragon 8 Gen 3",
        "ram": "12GB",
        "battery": "4900 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S24 Ultra",
        "display": "6.8 inch",
        "chipset": "Snapdragon 8 Gen 3",
        "ram": "12GB",
        "battery": "5000 mAh",
        "main_camera": "200 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S25",
        "display": "6.2 inch",
        "chipset": "Snapdragon 8 Elite",
        "ram": "12GB",
        "battery": "4000 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S25+",
        "display": "6.7 inch",
        "chipset": "Snapdragon 8 Elite",
        "ram": "12GB",
        "battery": "4900 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy S25 Ultra",
        "display": "6.9 inch",
        "chipset": "Snapdragon 8 Elite",
        "ram": "12GB / 16GB",
        "battery": "5000 mAh",
        "main_camera": "200 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy Note 20",
        "display": "6.7 inch",
        "chipset": "Exynos 990 / Snapdragon 865+",
        "ram": "8GB",
        "battery": "4300 mAh",
        "main_camera": "12 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy Note 20 Ultra",
        "display": "6.9 inch",
        "chipset": "Exynos 990 / Snapdragon 865+",
        "ram": "8GB / 12GB",
        "battery": "4500 mAh",
        "main_camera": "108 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy Z Fold 5",
        "display": "7.6 inch",
        "chipset": "Snapdragon 8 Gen 2",
        "ram": "12GB",
        "battery": "4400 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy Z Flip 5",
        "display": "6.7 inch",
        "chipset": "Snapdragon 8 Gen 2",
        "ram": "8GB",
        "battery": "3700 mAh",
        "main_camera": "12 MP",
        "source_url": "SOURCE_URL"
    },

    {
        "name": "Samsung Galaxy A54 5G",
        "display": "6.4 inch",
        "chipset": "Exynos 1380",
        "ram": "6GB / 8GB",
        "battery": "5000 mAh",
        "main_camera": "50 MP",
        "source_url": "SOURCE_URL"
    }
]


db = SessionLocal()


try:

    for phone_data in phones:

        # Check whether phone already exists
        existing_phone = (
            db.query(Phone)
            .filter(
                Phone.name == phone_data["name"]
            )
            .first()
        )

        if existing_phone:

            print(
                f"Already exists: "
                f"{phone_data['name']}"
            )

            continue

        phone = Phone(**phone_data)

        db.add(phone)

        print(
            f"Added: {phone_data['name']}"
        )

    db.commit()

    print("\nAll phones inserted successfully!")


except Exception as e:

    db.rollback()

    print("Error:", e)


finally:

    db.close()