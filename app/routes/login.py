from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.auth import authenticate_user, create_access_token

router = APIRouter()

# Схема для входящих данных
class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginData):
    # Аутентификация пользователя
    user = authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Генерация токена
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
