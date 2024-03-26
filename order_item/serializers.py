from rest_framework import serializers
from .models import *
from orders.serializers import OrdersSerializer
from products.serializers import ProductsSerializer


class Orders_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders_item
        fields = [
            'id',
            'user_id',
            'order_id',
            'product_id',
            'quantity',
            'comment',
        ]


class ReadOrderItemsSerializer(Orders_itemSerializer):
    product_id = ProductsSerializer(read_only=True)
