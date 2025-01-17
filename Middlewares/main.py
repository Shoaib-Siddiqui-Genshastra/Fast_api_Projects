from fastapi import FastAPI, HTTPException
from typing import List
from model import Employee
import crud
from middleware import LoggingMiddleware
#from middleware.logging import LoggingMiddleware
#from middleware.authentication import AuthenticationMiddleware
#from middleware.cors import add_cors_middleware
#from middleware.error_handling import ErrorHandlingMiddleware


app = FastAPI()

# Add middleware
app.add_middleware(LoggingMiddleware)

#app.add_middleware(AuthenticationMiddleware)
#app.add_middleware(ErrorHandlingMiddleware)
#add_cors_middleware(app)



@app.get("/employees/", response_model=List[Employee])
async def read_employees():
    return crud.read_employees()


@app.get("/employees/{employee_id}", response_model=Employee)
async def read_employee(employee_id: int):
    employee = crud.read_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees/", response_model=Employee)
async def create_employee(employee: Employee):
    return crud.create_employee(employee)


@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee: Employee):
    return crud.update_employee(employee_id, employee)


@app.delete("/employees/{employee_id}", response_model=Employee)
async def delete_employee(employee_id: int):
    return crud.delete_employee(employee_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)