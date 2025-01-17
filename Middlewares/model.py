from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: int
    name: str
    salary: float
    role: str
    contact_no: str
    address: str

# Example of creating an Employee instance
