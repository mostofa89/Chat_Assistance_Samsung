from app.database.connection import SessionLocal
from app.database.models import Phone


db = SessionLocal()


phone = Phone(
    name="Samsung Galaxy S23",
    display_size="6.1 inches",
    display_resolution="1080 x 2340 pixels",
    display_refresh_rate="120 Hz",
    chipset="Test chipset",
    ram="8 GB",
    storage="128 GB / 256 GB",
    main_camera="50 MP",
    ultrawide_camera="12 MP",
    telephoto_camera="10 MP",
    selfie_camera="12 MP",
    selfie_video="4K",
    battery="3900 mAh",
    charging="25W",
    os="Android",
    weight="168 g",
    price="Test price",
    source_url="https://example.com"
)


db.add(phone)

db.commit()

db.refresh(phone)

print("Phone inserted successfully!")
print("ID:", phone.id)
print("Name:", phone.name)


db.close()
