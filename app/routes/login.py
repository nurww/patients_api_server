from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.auth import authenticate_user, create_access_token

router = APIRouter()

# Schema for input data
class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginData):
    # User authentication
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Token generation
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
