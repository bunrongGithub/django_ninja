from django.http import HttpRequest

from ..model.locations_model import Locations
from ..schema.location_schema import LocationCreateSchema,LocationSchema


def create_location(_request: HttpRequest,payload: LocationCreateSchema) -> LocationSchema:
    created = Locations.objects.create(**payload.dict())
    return LocationSchema.model_validate(created)
