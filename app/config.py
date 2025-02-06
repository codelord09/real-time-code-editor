from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Authentication configuration
SECRET_KEY = os.getenv("SECRET_KEY")  # Ensure this matches the key in .env
ALGORITHM = os.getenv("ALGORITHM", "HS256")  # Default to HS256 if not set


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
