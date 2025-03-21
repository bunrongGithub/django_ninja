from ninja import NinjaAPI

from ..views.country_view import country_router
from ..views.location_view import location_router
from ..views.product_view import product_routes
from ..views.employee_view import employee_routes
from ..views.region_view import region_router
from ..views.job_view import job_router
from ..views.department_view import department_router

api = NinjaAPI()

api.add_router("products", product_routes)
api.add_router("employees", employee_routes)
api.add_router("regions", region_router)
api.add_router("jobs", job_router)
api.add_router("departments", department_router)
api.add_router("locations", location_router)
api.add_router("", country_router)
