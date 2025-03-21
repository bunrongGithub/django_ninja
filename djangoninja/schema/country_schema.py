from ninja import Schema

from djangoninja.schema.regions_schema import RegionsCreateSchema


class CountrySchema(Schema):
    id: int
    name: str
    region: RegionsCreateSchema


class CountriesCreateSchema(Schema):
    name: str
    region_id: int
