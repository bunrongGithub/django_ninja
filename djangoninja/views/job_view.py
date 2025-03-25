from django.http import HttpRequest
from ninja import Router

from djangoninja.schema.job_schema import JobSchema, JobCreateSchema
from djangoninja.services.job_service import create_job, get_job

router = Router()

router.tags = ["Jobs API"]
@router.post("/job", response=JobSchema)
def create(request: HttpRequest, payload: JobCreateSchema):
    created = create_job(payload)
    return created


@router.get("/job", response=list[JobSchema])
def get(request: HttpRequest):
    return get_job()
