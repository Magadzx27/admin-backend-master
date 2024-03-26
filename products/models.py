from django.db import models
from categories.models import *
from authentication.models import *


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='category_id',)
    images_urls = models.JSONField(max_length=10000, blank=False, null=False)
    name = models.CharField(max_length=500, blank=False, null=False)
    # price=models.FloatField(blank=False,null=False,default=None)
    description = models.TextField(max_length=20000, blank=True, null=True)
    # stock=models.IntegerField(blank=False,null=False,default=1)
    featured = models.BooleanField(default=False)
    # preorder = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # @property
    # def is_available(self):
    #     return self.stock > 0
