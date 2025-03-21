from ninja import Schema, ModelSchema
from ..model.jobs_model import Jobs
from decimal import Decimal


class JobSchema(Schema):
    id: int
    title: str
    min_salary: Decimal
    max_salary: Decimal


class JobCreateSchema(Schema):
    title: str
    min_salary: Decimal
    max_salary: Decimal
