from pydantic import EmailStr, ValidationError
from ninja import Schema
from decimal import Decimal
from typing import Optional

from djangoninja.schema.department_schema import DepartmentSchema
from djangoninja.schema.job_schema import JobSchema


class BaseAbstractSchema(Schema):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    job: JobSchema
    department: Optional[DepartmentSchema] = None
    salary: Decimal

    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def departments(self) -> Optional[DepartmentSchema]:
        return self.department

    def user_identify(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"Employee: {self.username()} (ID: {self.id})"


class ManagerSchema(BaseAbstractSchema):
    pass


class EmployeeSchema(BaseAbstractSchema):
    manager: Optional[ManagerSchema] = None
    department: Optional[DepartmentSchema] = None

    def departments(self) -> Optional[DepartmentSchema]:
        return super().departments()

    def username(self) -> str:
        return super().username()


class EmployeeCreateSchema(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    job_id: int
    salary: Decimal
    manager_id: Optional[int] = None
    department_id: Optional[int] = None

    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"Employee: {self.username()} (ID: {self.id})"
