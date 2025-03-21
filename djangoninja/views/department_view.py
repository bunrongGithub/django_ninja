from django.http import HttpRequest
from ninja import Router

from djangoninja.schema.department_schema import DepartmentSchema, DepartmentCreateSchema
from ..model.departments_model import Departments
department_router = Router()

@department_router.post('department', response=DepartmentSchema)
def create(request: HttpRequest,payload: DepartmentCreateSchema):
    created = Departments.objects.create(**payload.dict())
    return created