from django.http import HttpRequest
from ninja import Router
from djangoninja.services.employee_service import (
    list_employees,
    retrieve_employee,
    create_employee,
)
from djangoninja.schema.employee_schema import EmployeeSchema, EmployeeCreateSchema

router = Router()

# List all employees
_TGS = ["Employee API"]
router.tags = _TGS
@router.get("/employee", response=list[EmployeeSchema])
def get_employees(request: HttpRequest):
    return list_employees()


# Retrieve a specific employee by ID
@router.get("/employee/{employee_id}", response=EmployeeSchema)
def get_employee(request: HttpRequest, employee_id: int):
    return retrieve_employee(employee_id)


@router.post("/employee", response=EmployeeSchema)
def create(request: HttpRequest, payload: EmployeeCreateSchema):
    return create_employee(payload)
