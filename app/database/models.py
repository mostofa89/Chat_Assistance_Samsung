from sqlalchemy import Column, Integer, String, Text

from .connection import Base


class Phone(Base):

    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, index=True)

    # Basic
    name = Column(String(200), nullable=False, unique=True)
    release_date = Column(String(100))
    status = Column(String(100))
    source_url = Column(Text)

    # Network
    technology = Column(Text)
    two_g_bands = Column(Text)
    three_g_bands = Column(Text)
    four_g_bands = Column(Text)
    five_g_bands = Column(Text)
    speed = Column(Text)

    # Body
    dimensions = Column(Text)
    weight = Column(Text)
    build = Column(Text)
    sim = Column(Text)
    ip_rating = Column(String(100))

    # Display
    display_type = Column(Text)
    display_size = Column(String(100))
    display_resolution = Column(Text)
    display_protection = Column(Text)
    display_refresh_rate = Column(String(100))
    display_brightness = Column(Text)

    # Platform
    os = Column(Text)
    chipset = Column(Text)
    cpu = Column(Text)
    gpu = Column(Text)

    # Memory
    ram = Column(Text)
    storage = Column(Text)
    card_slot = Column(Text)

    # Main camera
    main_camera = Column(Text)
    ultrawide_camera = Column(Text)
    telephoto_camera = Column(Text)
    depth_camera = Column(Text)
    main_camera_features = Column(Text)
    main_camera_video = Column(Text)

    # Selfie
    selfie_camera = Column(Text)
    selfie_video = Column(Text)

    # Sound
    loudspeaker = Column(Text)
    headphone_jack = Column(Text)

    # Connectivity
    wlan = Column(Text)
    bluetooth = Column(Text)
    gps = Column(Text)
    nfc = Column(Text)
    radio = Column(Text)
    usb = Column(Text)

    # Sensors
    sensors = Column(Text)

    # Battery
    battery = Column(String(100))
    charging = Column(Text)
    wireless_charging = Column(Text)

    # Other
    colors = Column(Text)
    price = Column(Text)
    models = Column(Text)