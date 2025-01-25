from fastapi.testclient import TestClient
from app.main import app
from app.models import PatientDB
from sqlalchemy.orm import Session
from datetime import date, datetime

client = TestClient(app)

# Create test cases
def setup_test_data(db: Session):
    db.add_all([
        PatientDB(
            id=1,
            date_of_birth=date(1980, 1, 1),
            diagnoses='["Diabetes"]',
            created_at=datetime(2023, 1, 1, 12, 0, 0)
        ),
        PatientDB(
            id=2,
            date_of_birth=date(1990, 5, 15),
            diagnoses='["Asthma"]',
            created_at=datetime(2023, 1, 2, 12, 0, 0)
        ),
    ])
    db.commit()

def test_get_patients_success(test_db):
    # Creating test data
    setup_test_data(test_db)

    # Retrieve token
    login_response = client.post("/login", json={"username": "doctor", "password": "pass"})
    token = login_response.json()["access_token"]

    # Requesting a list of patients
    response = client.get("/patients", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_patients_access_denied(test_db):
    # Retrieve token for user without role `doctor`
    login_response = client.post("/login", json={"username": "admin", "password": "pass"})
    token = login_response.json()["access_token"]

    # Trying to request a list of patients
    response = client.get("/patients", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
    assert response.json()["detail"] == "Access denied"

def test_get_patients_unauthorized():
    response = client.get("/patients")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
