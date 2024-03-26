from rest_framework import serializers
from .models import *
from products.serializers import ProductsSerializer


class CartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carts
        fields = [
            'id',
            'user_id',
            'product_id',
            'quantity',
            'comment'
        ]

class ReadCartsSerializer(CartsSerializer):
    product_id = ProductsSerializer(read_only=True)
    
# class CartsSelect(serializers.ModelSerializer)

#     Cart.objects.select_related('product__price').annotate(
#         sum= ExpressionWrapper(
#         F('product__price__value') * F('qnt'), output_field=DecimalField()))