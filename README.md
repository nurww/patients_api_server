# Patients API Server

## Overview
API-server that manages patients data:
- `/login`: Obtain a JWT token.
- `/patients`: Retrieve a list of patients (accessible only to doctors).

## Project Structure
- `app/`: Source code.
- `tests/`: Unit tests.
- `migrations/`: Database migrations.
- `requirements.txt`: Project dependencies.

## Installation and launch
1. Install dependencies:
   pip install -r requirements.txt
2. Apply database migrations:
   alembic upgrade head
3. Start the server:
   uvicorn app.main:app --reload
4. Access the API at: http://localhost:8000.

## Running with Docker
1. Check Docker installation:
   docker --version
2. Build the Docker image:
   docker build -t patients-api .
3. Run the container:
   docker run -d -p 8000:8000 patients-api
4. Access the API at: http://localhost:8000.

## API Examples
### /login
   #### Request:
   ```
   curl -X POST http://localhost:8000/login \
   -H "Content-Type: application/json" \
   -d '{"username": "doctor", "password": "pass"}'
   ```
   #### Response:
   ```
   {
      "access_token": "eyJhbGciOiJIUzI1...",
      "token_type": "bearer"
   }
   ```

### /patients
   #### Request:
   ```
   curl -X GET http://localhost:8000/patients \
   -H "Authorization: Bearer <ACCESS_TOKEN>"
   ```
   #### Response:
   ```
   [
      {
         "id": 1,
         "date_of_birth": "1980-01-01",
         "diagnoses": ["Diabetes"],
         "created_at": "2023-01-01T12:00:00"
      },
      ...
   ]
   ```

## Testing
### Run the tests using:
   ```
   pytest --cov=app tests/
   ```
### A coverage report will be displayed after the tests complete.

## Configuration `alembic.ini`
To configure Alembic migrations, ensure the `sqlalchemy.url` in `alembic.ini` points to your database:

```ini
sqlalchemy.url = mysql+pymysql://root:root@localhost/mad_devs
```

## Configuration `migrations/env.py`
Ensure the metadata is linked to your database models:

```ini
from app.models import Base

target_metadata = Base.metadata
```

# Category Sales Calculator

## Usage

### Navigate to the `category_sales_calculator` directory:
```
cd category_sales_calculator
```

### Place a JSON file with sales data in this directory. The file must adhere to the following format:
```
[
  {
    "id": 1,
    "owner": "user2",
    "price": 8647,
    "category": "cat1"
  },
  ...
]
```
### Run the calculator:
```
python category_sales_calculator.py
```
### The output will display the number of items and total sales per category:
```
Number of items by category:
{'cat1': 333103, 'cat3': 333386, 'cat2': 333511}

Total sales by category:
{'cat1': 1831348772, 'cat3': 1832844186, 'cat2': 1832867646}
```