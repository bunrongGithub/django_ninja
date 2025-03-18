from ninja import NinjaAPI
from ..views.product_view import router

api =  NinjaAPI()

api.add_router("/store",router)