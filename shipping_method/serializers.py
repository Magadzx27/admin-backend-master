from rest_framework import serializers
from .models import *


class Shipping_methodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping_method
        fields = [
            'id',
            'name',
            'image_url',
            'contact_number',
            'info_message',
            'price',
            'deleted'
        ]
