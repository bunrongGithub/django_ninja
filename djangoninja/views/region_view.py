from django.http import HttpRequest
from ..schema.regions_schema import RegionsSchema, RegionsCreateSchema
from ..services.region_service import create_region, get_region
from ninja import Router

router = Router()

router.tags = ['Regions API']
@router.post("", response=RegionsSchema)
def creat(request: HttpRequest, payload: RegionsCreateSchema) -> RegionsSchema:
    created = create_region(payload)
    return created


@router.get("", response=list[RegionsSchema])
def get_regions(request: HttpRequest):
    return get_region()
