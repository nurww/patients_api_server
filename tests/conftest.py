import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.main import app
from app.database import get_db

# Настройка тестовой базы данных
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц тестовой базы
def init_test_db():
    Base.metadata.create_all(bind=engine)

def cleanup_test_db():
    Base.metadata.drop_all(bind=engine)
    
@pytest.fixture(scope="module")
def test_db():
    init_test_db()
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        cleanup_test_db()

@pytest.fixture(scope="module", autouse=True)
def override_dependency():
    # Явное переопределение зависимости для тестов
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
