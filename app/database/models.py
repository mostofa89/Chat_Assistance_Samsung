from sqlalchemy import Column, Integer, String, Text

from .connection import Base


class Phone(Base):

    __tablename__ = "phones"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(200),
        nullable=False,
        unique=True
    )

    release_date = Column(String(100))

    display = Column(Text)

    resolution = Column(Text)

    refresh_rate = Column(String(100))

    chipset = Column(Text)

    ram = Column(String(100))

    storage = Column(Text)

    main_camera = Column(Text)

    ultrawide_camera = Column(Text)

    telephoto_camera = Column(Text)

    selfie_camera = Column(Text)

    video = Column(Text)

    battery = Column(String(100))

    charging = Column(String(100))

    operating_system = Column(String(200))

    weight = Column(String(100))

    price = Column(String(200))

    source_url = Column(Text)