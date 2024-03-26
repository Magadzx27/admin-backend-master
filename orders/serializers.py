from rest_framework import serializers
from .models import *


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = [
            'id',
            'user_id',
            'shipping_id',
            'payment_id',
            'user_name',
            'user_address',
            'user_phone',
            'date',
            'store_status',
            'user_status',
            'total',
        ]
