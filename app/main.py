from fastapi import FastAPI
from app.routes import login, patients

app = FastAPI()

# Connecting routes
app.include_router(login.router)
app.include_router(patients.router)
