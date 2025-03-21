from django.http import JsonResponse
from django.http import HttpRequest
from ninja import Router
from djangoninja.schema.product_schema import ProductCreateSchema,ProductSchema
from djangoninja.services.product_service import get_all_products,create_product,get_product_by_id

product_routes = Router()

@product_routes.get("/products",response=list[ProductSchema])
async def list_products(request):
    return await get_all_products()

@product_routes.post("/product",response=ProductSchema)
async def create_new_product(request,payload: ProductCreateSchema):
    return await create_product(payload)
    
@product_routes.get("/product/{product_id}",response=ProductSchema)
async def get_product(request: HttpRequest,product_id: int):
    product = await get_product_by_id(product_id)
    if not product:
        return JsonResponse({"msg":"Product not found"}, status=404)
    return product