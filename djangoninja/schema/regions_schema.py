from ninja import ModelSchema,Schema
from ..model.regions_model import Regions
class RegionsSchema(Schema):
   id: int
   name: str

class RegionsCreateSchema(Schema):
   name: str