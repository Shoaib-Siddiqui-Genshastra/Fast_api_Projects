from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: int
    name: str
    salary: float
    role: str
    contact_no: str
    address: str

# Example of creating an Employee instance
employee = Employee(
    employee_id=1,
    name="John Doe",
    salary=50000.0,
    role="Software Engineer",
    contact_no="123-456-7890",
    address="123 Main Street, Bengaluru, Karnataka"
)

print(employee)
