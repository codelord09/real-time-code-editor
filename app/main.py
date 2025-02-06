from fastapi import FastAPI, WebSocket, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
from app.models import Base
from app.schemas import UserCreate, CodeFileCreate
from app.crud import create_user, create_code_file
from app.websocket import ConnectionManager
from app.ai_debugger import get_debugging_suggestions
from app.auth import get_current_user
from app.config import get_db


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Socket.IO
socket_manager = SocketManager(app=app)
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


@app.post("/debug/")
def debug_code(code: str):
    suggestions = get_debugging_suggestions(code)
    return {"suggestions": suggestions}


# Socket.IO Event Handlers
@app.sio.on("join")
async def handle_join(sid, *args):
    print(f"Client {sid} joined")
    await app.sio.emit("message", f"Welcome Client {sid}")


@app.sio.on("send_message")
async def handle_send_message(sid, data):
    print(f"Message from {sid}: {data}")
    await app.sio.emit("receive_message", data)


@app.sio.on("disconnect")
async def handle_disconnect(sid):
    print(f"Client {sid} disconnected")


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except Exception:
        manager.disconnect(websocket)
