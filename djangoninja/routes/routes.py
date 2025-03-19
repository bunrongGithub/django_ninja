from ninja import NinjaAPI
from ..views.product_view import product_routes
from ..views.employee_view import employee_routes

api =  NinjaAPI()

api.add_router("product",product_routes)
api.add_router("employee",employee_routes)