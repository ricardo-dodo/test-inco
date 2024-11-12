from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    birth_date = Column(Date)
    department = Column(String)
    position = Column(String)
    is_active = Column(Boolean, default=True) 