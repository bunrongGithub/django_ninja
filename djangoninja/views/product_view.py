from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse
from ninja import Router
from djangoninja.schema.product_schema import ProductCreateSchema,ProductSchema
from djangoninja.services.product_service import get_all_products,create_product,get_product_by_id


router = Router()

@router.get("product",response=list[ProductSchema])
def list_products(request):
    return get_all_products()

@router.post("/products",response=ProductSchema)
def create_new_product(request,payload: ProductCreateSchema):
    return create_product(payload)
    
@router.get("/product/{product_id}",response=ProductSchema)
async def get_product(request: HttpRequest,product_id: int):
    product = await get_product_by_id(product_id)
    if not product:
        return JsonResponse({"msg":"Product not found"}, status=404)
    return product