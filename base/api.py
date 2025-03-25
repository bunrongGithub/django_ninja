
from auths.api import router as auths_router
from djangoninja.routes.routes import *
from ninja import NinjaAPI
api = NinjaAPI()

api.add_router("auth/",auths_router)
api.add_router("countries/",country_router)
api.add_router("locations/",location_router)
api.add_router("employees/",employee_routes)
api.add_router("regions/",region_router)
api.add_router("products/",product_routes)
api.add_router("jobs/",job_router)
api.add_router("departments/",department_router)