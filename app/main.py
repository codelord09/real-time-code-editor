from fastapi import FastAPI, WebSocket, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base
from app.schemas import UserCreate, CodeFileCreate
from app.crud import create_user, create_code_file
from app.websocket import ConnectionManager
from app.ai_debugger import get_debugging_suggestions
from app.auth import get_current_user
from app.config import get_db
from pydantic import BaseModel


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.1.21:3000",
        "http://localhost:3000",
    ],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()


@app.get("/")
def read_root():
    return {"message": "Real-Time Collaborative Code Editor is running!"}


@app.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@app.post("/code/")
def create_code(
    file: CodeFileCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_code_file(db, file, current_user.id)


# Define a Pydantic model for the input data
class CodeRequest(BaseModel):
    code: str


@app.post("/debug/")
def debug_code(code: CodeRequest):
    print(f"Received code: {code.code}")  # Log the incoming code

    """
    Endpoint to generate AI-powered debugging suggestions.

    Args:
        code (dict): JSON payload containing the code snippet.
                     Example: {"code": "def add(a, b): return a - b"}

    Returns:
        dict: AI-generated debugging suggestions.
    """
    try:
        code_snippet = (
            code.code
        )  # Access the code using the 'code' attribute of CodeRequest model
        if not code_snippet:
            raise ValueError("Code snippet is required.")

        suggestions = get_debugging_suggestions(code_snippet)
        return {"suggestions": suggestions}
    except Exception as e:
        return {"error": str(e)}


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except Exception:
        manager.disconnect(websocket)
