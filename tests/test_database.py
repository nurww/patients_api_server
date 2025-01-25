from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import Base
from app.database import get_db

# Подключение к тестовой базе данных
TEST_DATABASE_URL = "sqlite:///./test.db"  # SQLite для тестов
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаём таблицы для тестов
def init_test_db():
    Base.metadata.create_all(bind=engine)
