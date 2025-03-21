from ninja import Schema

from djangoninja.schema.location_schema import LocationSchema


class DepartmentSchema(Schema):
    id: int
    name: str
    location: LocationSchema


class DepartmentCreateSchema(Schema):
    name: str
    location_id: int
