from django.http import HttpRequest

from ..schema.location_schema import LocationSchema, LocationCreateSchema
from ..services.location_service import create_location

from ninja import Router

router = Router()

_TGS = ["Location Api"]
@router.post("",tags=_TGS, response=LocationSchema)
def create(request: HttpRequest, payload: LocationCreateSchema):
    return create_location(request, payload)
