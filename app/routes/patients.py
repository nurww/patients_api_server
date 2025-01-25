from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.models import Patient

router = APIRouter()

# Patient data for example
fake_patients_db = [
    {"id": 1, "date_of_birth": "1980-01-01", "diagnoses": ["Diabetes"], "created_at": "2023-01-01T12:00:00"},
    {"id": 2, "date_of_birth": "1990-05-15", "diagnoses": ["Asthma"], "created_at": "2023-01-02T12:00:00"},
]

@router.get("/patients", response_model=list[Patient])
def get_patients(current_user: dict = Depends(get_current_user)):
    # Check that the user has the `doctor` role
    if current_user["role"] != "doctor":
        raise HTTPException(status_code=403, detail="Access denied")
    return fake_patients_db
