from rest_framework import serializers
from .models import *


class Payment_methodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment_method
        fields = [
            'id',
            'name',
            'image_url',
            'info_message',
            'deleted'
        ]
