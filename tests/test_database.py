from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import Base

# Connecting to a test database
TEST_DATABASE_URL = "sqlite:///./test.db"  # SQLite for tests
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating tables for tests
def init_test_db():
    Base.metadata.create_all(bind=engine)
