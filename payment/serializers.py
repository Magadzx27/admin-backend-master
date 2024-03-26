from rest_framework import serializers
from .models import *
from shipping.serializers import ShippingSerializer
from orders.serializers import OrdersSerializer


class PaymentSerializer(serializers.ModelSerializer):
    # shipping = serializers.PrimaryKeyRelatedField(read_only=True)
    # shipping = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id',
            'user_id',
            'order_id',
            'date',
            'amount',
            'comment'   
        ]
