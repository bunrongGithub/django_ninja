from ..model.models import Product
def get_all_products():
    try:
        product_list =  Product.objects.all()
        return product_list
    except Product.DoesNotExist:
        return None

def create_product(data):
    return Product.objects.create(**data.dict())

async def get_product_by_id(product_id):
    try:
        return await Product.objects.aget(id=product_id)
    except Product.DoesNotExist:
        return None