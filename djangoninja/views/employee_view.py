from django.http import HttpRequest
from ninja import Router
from djangoninja.services.employee_service import list_employees, retrieve_employee,create_employee
from djangoninja.schema.employee_schema import EmployeeSchema, EmployeeCreateSchema

employee_routes = Router()

# List all employees

@employee_routes.get("/employee", response=list[EmployeeSchema])
def get_employees(request: HttpRequest):
    return list_employees()

# Retrieve a specific employee by ID
@employee_routes.get("/employee/{employee_id}", response=EmployeeSchema)
def get_employee(request: HttpRequest, employee_id: int):
    return retrieve_employee(employee_id)

@employee_routes.post("/employee", response=EmployeeSchema)
def create(request: HttpRequest,payload: EmployeeCreateSchema):
    return create_employee(payload)