from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

# Конфигурация JWT
SECRET_KEY = "your_secret_key"  # Секретный ключ для подписания токенов
ALGORITHM = "HS256"            # Алгоритм шифрования
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Время жизни токена (30 минут)

# Данные пользователей
fake_users_db = {
    "doctor": {"username": "doctor", "password": "pass", "role": "doctor"},
    "admin": {"username": "admin", "password": "pass", "role": "admin"}
}

# Проверка логина и пароля
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return user
    return None

# Генерация JWT-токена
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Используем `OAuth2PasswordBearer` для извлечения токена из запроса
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Проверка токена и роли пользователя
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username, "role": role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")