from ninja import Schema
from decimal import Decimal
from datetime import datetime

class ProductSchema(Schema):
    id: int 
    name: str
    description: str 
    price: Decimal
    stock: int 
    created_at: datetime

class ProductCreateSchema(Schema):
    name: str 
    description: str 
    price: Decimal
    stock: int

