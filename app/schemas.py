from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class CodeFileCreate(BaseModel):
    filename: str
    content: str


class CodeFileResponse(BaseModel):
    id: int
    filename: str
    content: str
    owner_id: int
