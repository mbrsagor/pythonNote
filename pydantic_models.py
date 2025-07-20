from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field


# Enum for Department choices
class Department(str, Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


# Employee data model
class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4)
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool


# Example usage
if __name__ == "__main__":
    emp = Employee(
        name="Alice Johnson",
        email="alice.johnson@example.com",
        date_of_birth=date(1990, 5, 15),
        salary=85000.00,
        department=Department.ENGINEERING,
        elected_benefits=True
    )
    
    print(emp)
    print(f"Employee ID: {emp.employee_id}")


