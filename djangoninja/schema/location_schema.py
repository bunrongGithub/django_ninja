from ninja import Schema

from djangoninja.schema.country_schema import CountrySchema


class LocationSchema(Schema):
    id: int
    street_address: str
    postal_code: str
    city: str
    state_province: str
    country: CountrySchema
    def get_location_info(self)-> str:
        return f"{self.country.name}, {self.country.region.name}, {self.city}, {self.state_province}, {self.postal_code}"

class LocationCreateSchema(Schema):
    street_address: str
    postal_code: str
    city: str
    state_province: str
    country_id: int