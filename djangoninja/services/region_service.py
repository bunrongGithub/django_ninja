from ..model.regions_model import Regions
from ..schema.regions_schema import RegionsCreateSchema,RegionsSchema


def create_region(payload: RegionsCreateSchema) -> RegionsSchema:
    validated = RegionsSchema.model_validate(payload)
    created = Regions.objects.create(**validated.model_dump())
    return RegionsSchema.model_validate(created)

def get_region() -> list[RegionsSchema]:
    regions = Regions.objects.all()
    return [RegionsSchema.from_orm(origin) for origin in regions]
