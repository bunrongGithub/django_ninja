from django.http import HttpRequest
from ninja import Router

from djangoninja.schema.country_schema import CountrySchema, CountriesCreateSchema
from djangoninja.services.contry_service import create_countries

router = Router()

_TGS = ["Country API"]
@router.post("",tags=_TGS, response=CountrySchema)
def create(request: HttpRequest, payload: CountriesCreateSchema):
    return create_countries(request, payload)
