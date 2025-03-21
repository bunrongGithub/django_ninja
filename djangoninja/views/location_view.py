from django.http import HttpRequest

from ..schema.location_schema import LocationSchema, LocationCreateSchema
from ..services.location_service import create_location

from ninja import Router
location_router = Router()

@location_router.post("location",response=LocationSchema)
def create(request: HttpRequest,payload: LocationCreateSchema):
    return create_location(request,payload)
