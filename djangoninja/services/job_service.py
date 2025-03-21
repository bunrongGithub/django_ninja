from ..model.jobs_model import Jobs
def create_job(payload):
    create = Jobs.objects.create(**payload.dict())
    return create

def get_job():
    return Jobs.objects.all()