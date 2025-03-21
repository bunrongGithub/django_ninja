from django.http import HttpRequest
from ninja import Router

from djangoninja.schema.country_schema import CountrySchema, CountriesCreateSchema
from djangoninja.services.contry_service import create_countries

country_router = Router()


@country_router.post("/create-countries", response=CountrySchema)
def create(request: HttpRequest, payload: CountriesCreateSchema):
    return create_countries(request, payload)
