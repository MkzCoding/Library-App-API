from fastapi import APIRouter, HTTPException
from app.schemas.request.login import UserLogIn
from app.utils.security import verify_password
from app.db.member_repo import get_member_by_username
from app.db.librarian_repo import get_librarian_by_username
from app.schemas.response.login import UserLogInResponse, TokenResponse
from jose import jwt 
import os 
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM  = os.getenv("ALGORITHM")

@router.post("/member", response_model= TokenResponse)
def user_login(user: UserLogIn):
    user_db = get_member_by_username(user.username)
    if not user_db:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    if not verify_password(user.password, user_db["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials."
        )
    else:
        payload = {
            "sub":user_db["username"],
            "role":"member",
            "exp": datetime.now() + timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type":"bearer"}
@router.post("/librarian", response_model= TokenResponse)
def user_login(user: UserLogIn):
    user_db = get_librarian_by_username(user.username)
    if not user_db:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    if not verify_password(user.password, user_db["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials."
        )
    else:
        payload = {
            "sub": user_db["username"],
            "role":user_db["role"],
            "exp": datetime.now() + timedelta(minutes= 30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
