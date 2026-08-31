from app.database.connection import engine, Base
from app.database.models import Phone


print("Creating database tables...")


Base.metadata.create_all(
    bind=engine
)


print("Tables created successfully!")