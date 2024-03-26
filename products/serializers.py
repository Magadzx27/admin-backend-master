from rest_framework import serializers
from .models import *
from categories.serializers import CategoriesSerializer


class ProductsSerializer(serializers.ModelSerializer):
    # category_id = CategoriesSerializer()
    #category_id = serializers.PrimaryKeyRelatedField(read_only=True)
    #category_id = serializers.StringRelatedField(read_only=True)
    # category_id = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='name'
    # )

    class Meta:
        model = Products
        fields = [
            'id',
            'created_date',
            'category_id',
            'name',
            # 'price',
            'description',
            'images_urls',
            # 'stock',
            'featured',
            # 'preorder',
            'active',
            'deleted',
        ]
