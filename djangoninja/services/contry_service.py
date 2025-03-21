from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ..model import Countries, Regions
from ..schema.country_schema import CountriesCreateSchema,CountrySchema


def create_countries(_request: HttpRequest,payload: CountriesCreateSchema) -> CountrySchema:
    region = get_object_or_404(Regions,id=payload.region_id)
    print(region)
    created = Countries.objects.create(name=payload.name,region=region)
    return CountrySchema.model_validate(created)
