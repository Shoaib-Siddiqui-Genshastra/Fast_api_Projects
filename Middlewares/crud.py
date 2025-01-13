import json
from typing import List, Optional
from model import Employee

DATABASE_FILE = "database.json"

def read_employees() -> List[Employee]:
    try:
        with open(DATABASE_FILE, "r") as f:
            employees = json.load(f)
        return [Employee(**employee) for employee in employees]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_employee(employee_id: int) -> Optional[Employee]:
    employees = read_employees()
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    return None

def create_employee(employee: Employee) -> Employee:
    employees = read_employees()
    employees.append(employee)
    with open(DATABASE_FILE, "w") as f:
        json.dump([employee.dict() for employee in employees], f)
    return employee

def update_employee(employee_id: int, updated_employee: Employee) -> Employee:
    employees = read_employees()
    for i, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            employees[i] = updated_employee
            with open(DATABASE_FILE, "w") as f:
                json.dump([employee.dict() for employee in employees], f)
            return updated_employee
    raise ValueError("Employee not found")

def delete_employee(employee_id: int) -> Employee:
    employees = read_employees()
    for i, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            deleted_employee = employees.pop(i)
            with open(DATABASE_FILE, "w") as f:
                json.dump([employee.dict() for employee in employees], f)
            return deleted_employee
    raise ValueError("Employee not found")



"""
import json
from typing import List, Optional
from model import Employee

DATABASE_FILE = "database.json"


def read_employees() -> List[Employee]:
    with open(DATABASE_FILE, "r") as f:
        employees = json.load(f)
    return [Employee(**employee) for employee in employees]


def read_employee(employee_id: int) -> Optional[Employee]:
    employees = read_employees()
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    return None


def create_employee(employee: Employee) -> Employee:
    employees = read_employees()
    employees.append(employee)
    with open(DATABASE_FILE, "w") as f:
        json.dump([employee.dict() for employee in employees], f)
    return employee


def update_employee(employee_id: int, updated_employee: Employee) -> Employee:
    employees = read_employees()
    for i, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            employees[i] = updated_employee
            with open(DATABASE_FILE, "w") as f:
                json.dump([employee.dict() for employee in employees], f)
            return updated_employee
    raise ValueError("Employee not found")


def delete_employee(employee_id: int) -> Employee:
    employees = read_employees()
    for i, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            deleted_employee = employees.pop(i)
            with open(DATABASE_FILE, "w") as f:
                json.dump([employee.dict() for employee in employees], f)
            return deleted_employee
    raise ValueError("Employee not found")

raise ValueError("Employee not found")
"""