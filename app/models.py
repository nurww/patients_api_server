from sqlalchemy import Column, Integer, Date, DateTime, Text, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

# SQLAlchemy Base для работы с таблицами базы данных
Base = declarative_base()

# Модель для таблицы `patients`
class PatientDB(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    date_of_birth = Column(Date, nullable=False)
    diagnoses = Column(Text, nullable=False)  # Храним список диагнозов в текстовом виде
    created_at = Column(DateTime, nullable=False)

# URL подключения к базе данных
DATABASE_URL = "mysql+pymysql://root:root@localhost/mad_devs"

# Настройка SQLAlchemy движка и сессии
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для создания таблиц в базе данных
def create_tables():
    Base.metadata.create_all(bind=engine)

# Модель для сериализации данных
class Patient(BaseModel):
    id: int
    date_of_birth: date
    diagnoses: list[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
