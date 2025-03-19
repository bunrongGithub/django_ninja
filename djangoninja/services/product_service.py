from django.http import JsonResponse

from ..model.product_model import Product
def get_all_products():
    try:
        product_list =  Product.objects.all()
        return product_list
    except Product.DoesNotExist:
        return None

def create_product(data):
    create = Product.objects.create(**data.dict())
    if create:
        return JsonResponse({"mgs":"Created"},status=201)

async def get_product_by_id(product_id):
    try:
        return await Product.objects.aget(id=product_id)
    except Product.DoesNotExist:
        return None