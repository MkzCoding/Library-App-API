from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError, ExpiredSignatureError
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM  = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


PUBLIC_PATHS = ["/login/member", "/login/librarian", "/registration", "/docs", "/openapi.json"]
async def auth_middleware(request: Request, call_next):
    path = request.url.path
    if any(path.startswith(p) for p in PUBLIC_PATHS):
        return await call_next(request)
        
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
       
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms = [ALGORITHM])
        request.state.user = {"id": payload.get("sub"), "role": payload.get("role")}
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Tokem Expired.")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token.")
    
    response = await call_next(request)
    return response