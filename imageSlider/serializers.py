from rest_framework import serializers
from .models import *


class ImagesliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imageslider
        fields = [
            'id',
            'image_url',
            'title',
            'subtitle',
            'display_order',
        ]
