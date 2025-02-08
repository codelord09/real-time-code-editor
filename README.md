# Real-Time Collaborative Code Editor with AI-Assisted Debugging

This repository contains the implementation of a **Real-Time Collaborative Code Editor with AI-Assisted Debugging**, built using **FastAPI** for the backend and **React** for the frontend. The platform allows multiple developers to collaborate on code in real-time (like Google Docs for code) and provides AI-powered debugging suggestions using **Qwen 2.5 7B** running locally via **Ollama**.

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Folder Structure](#folder-structure)
4. [Setup Instructions](#setup-instructions)
   - [Backend Setup](#backend-setup)
   - [Frontend Setup](#frontend-setup)
5. [Running the Application](#running-the-application)
6. [API Documentation](#api-documentation)
7. [Testing](#testing)
8. [Docker Setup (Optional)](#docker-setup-optional)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

### Core Features

1. **Real-Time Collaboration**:
   - Multiple users can edit the same code file simultaneously.
   - Changes are synced in real-time using WebSockets.
   - Live cursors and highlights for each user.

2. **AI-Assisted Debugging**:
   - Integrates **Qwen 2.5 7B** (via **Ollama**) to analyze code locally.
   - Provides real-time suggestions for syntax errors, potential bugs, and performance improvements.
   - Users can accept or reject AI suggestions.

3. **User Management**:
   - User registration and login.
   - Role-based access control (e.g., owner, collaborator).

4. **Scalability and Performance**:
   - Uses Redis for caching and RabbitMQ for message queuing.
   - Optimized database queries and rate limiting for AI service.

5. **Security**:
   - Authentication and authorization using JWT tokens.
   - Input sanitization to prevent injection attacks.

6. **Bonus Features**:
   - Frontend interface built with React for visualizing the code editor and AI suggestions.
   - Optional Git-like version control for code files.

---

## Requirements

### Prerequisites

- Python 3.9+
- Node.js (for the frontend)
- PostgreSQL (for the database)
- Redis (for caching and real-time updates)
- RabbitMQ (optional, for message queuing)
- Docker (optional, for containerization)
- **Ollama** installed locally for running **Qwen 2.5 7B**

### Dependencies

- Backend: FastAPI, SQLAlchemy, Pydantic, Uvicorn, Redis, RabbitMQ, etc.
- Frontend: React, Socket.IO, CodeMirror, Axios, etc.

---

## Folder Structure

```
real-time-code-editor/
├── app/                     # Backend (FastAPI)
│   ├── main.py              # Main entry point
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # CRUD operations
│   ├── websocket.py         # WebSocket implementation
│   ├── ai_debugger.py       # AI integration (Qwen 2.5 7B via Ollama)
│   ├── auth.py              # Authentication and authorization
│   ├── config.py            # Configuration settings
│   └── utils/               # Utility functions
├── frontend/                # Frontend (React)
│   ├── public/              # Static assets
│   ├── src/                 # React source code
│   │   ├── components/      # React components
│   │   ├── App.js           # Main application component
│   │   └── index.js         # Entry point
│   ├── package.json         # Dependencies
│   └── README.md            # Frontend documentation
├── migrations/              # Database migrations
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md                # Project documentation
```

---

## Setup Instructions

### Backend Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up PostgreSQL**:
   - Create a database named `code_editor`.
   - Update the `.env` file with your PostgreSQL credentials:
     ```env
     DATABASE_URL=postgresql://user:password@localhost/code_editor
     ```

3. **Set Up Redis**:
   - Start Redis locally or use a hosted instance.

4. **Install Ollama and Qwen 2.5 7B**:
   - Install **Ollama** by following the instructions at [Ollama's official website](https://ollama.ai/).
   - Pull the **Qwen 2.5 7B** model:
     ```bash
     ollama pull qwen2.5:7b
     ```

5. **Update `.env`**:
   - Add the following to your `.env` file:
     ```env
     OLLAMA_MODEL=qwen2.5:7b
     ```

6. **Run Migrations**:
   - Use Alembic or SQLAlchemy to create tables in the database.

### Frontend Setup

1. **Navigate to the Frontend Directory**:
   ```bash
   cd frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Start the Development Server**:
   ```bash
   npm start
   ```

---

## Running the Application

### Backend

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```
The backend will run at `http://localhost:8000`.

### Frontend

Start the React development server:
```bash
npm start
```
The frontend will run at `http://localhost:3000`.

---

## API Documentation

Access the Swagger UI documentation at:
```
http://localhost:8000/docs
```
This includes all APIs for user management, code file management, and AI debugging.

---

## Testing

### Backend Tests

Run unit and integration tests using `pytest`:
```bash
pytest
```

### Frontend Tests

Use tools like Jest or React Testing Library for frontend testing.

---

## Docker Setup (Optional)

1. **Build and Start Containers**:
   ```bash
   docker-compose up --build
   ```

2. **Access the Application**:
   - Backend: `http://localhost:8000`
   - Frontend: `http://localhost:3000`

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---
### Notes on AI Integration

- The AI model (**Qwen 2.5 7B**) is run locally using **Ollama**, ensuring data privacy and eliminating dependency on external APIs.
- To call the model, the backend uses a subprocess or HTTP requests to interact with the Ollama server.
