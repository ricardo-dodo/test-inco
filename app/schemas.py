from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    birth_date: date
    department: str
    position: str
    is_active: bool = True

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    birth_date: Optional[date] = None
    department: Optional[str] = None
    position: Optional[str] = None
    is_active: Optional[bool] = None

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "birth_date": "1990-01-01",
                "department": "IT",
                "position": "Developer",
                "is_active": True
            }
        }