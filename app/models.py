from sqlalchemy import Column, Integer, Date, DateTime, Text, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, ConfigDict
from datetime import date, datetime

# SQLAlchemy Base for working with database tables
Base = declarative_base()

# Model for table `patients`
class PatientDB(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    date_of_birth = Column(Date, nullable=False)
    diagnoses = Column(Text, nullable=False)  # We store the list of diagnoses in text form
    created_at = Column(DateTime, nullable=False)

# Database connection URL
DATABASE_URL = "mysql+pymysql://root:root@localhost/mad_devs"

# Setting up SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function for creating tables in a database
def create_tables():
    Base.metadata.create_all(bind=engine)

# Model for data serialization
class Patient(BaseModel):
    id: int
    date_of_birth: date
    diagnoses: list[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
