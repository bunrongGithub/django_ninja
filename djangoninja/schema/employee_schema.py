from pydantic import EmailStr,ValidationError
from ninja import Schema
from decimal import Decimal
class EmployeeSchema(Schema):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    job: int
    salary: Decimal
    manager: int
    department: int

class EmployeeCreateSchema(Schema):
    first_name:str 
    last_name: str 
    email: EmailStr
    phone_number: str 
    job: int 
    salary: Decimal
    manager: int 
    department: int 

data = dict(
    id=1,
    first_name="John",
    last_name="Doe",
    email="<EMAIL>",
    phone_number="0123456789",
    job=1,
    salary=20000,
    manager=2,
    department=3
)
try:
    EmployeeCreateSchema.model_validate({
        "field":"invalid"
    })
except ValidationError as e:
    print(repr(e.errors()[0]["type"]))