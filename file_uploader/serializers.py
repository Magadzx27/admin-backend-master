from rest_framework import serializers
from .models import UploderModel

class UploderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploderModel
        fields = "__all__"