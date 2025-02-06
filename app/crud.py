from sqlalchemy.orm import Session
from app.models import User, CodeFile
from app.schemas import UserCreate, CodeFileCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username, hashed_password=user.password
    )  # Hash password in production
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_code_file(db: Session, file: CodeFileCreate, user_id: int):
    db_file = CodeFile(filename=file.filename, content=file.content, owner_id=user_id)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
