# Library App

A FastAPI-based library management system with JWT authentication and role-based authorization (members and librarians).

---

## Features

- User registration and login with JWT tokens
- Role-based access control (member vs librarian)
- Book management endpoints
- SQLite database backend
- Swagger UI for interactive API docs

---

## Tech Stack

- **FastAPI** for API framework
- **SQLite** for database
- **python-jose** for JWT handling
- **Pydantic** for request/response models

---

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/library_app.git
   cd library_app
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create an env file:
   ```bash
   SECRET_KEY=your_secret_key_here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

7. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
