from rest_framework import serializers
from .models import Review
from authentication.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'id',
            'date',
            'item_id',
            'user_id',
            'comment',
            'rating',
            'deleted'
        ]


class ReadReviewsSerializer(ReviewSerializer):
    user_id = UserSerializer(read_only=True)
