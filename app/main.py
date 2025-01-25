from fastapi import FastAPI
from app.routes import login, patients

app = FastAPI()

# Подключение маршрутов
app.include_router(login.router)
app.include_router(patients.router)
