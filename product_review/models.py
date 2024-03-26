from django.db import models
from products.models import *
from authentication.models import *


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    item_id = models.ForeignKey(
        Products, on_delete=models.CASCADE, db_column='product_id')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='user_id')
    comment = models.CharField(max_length=1500, blank=False, null=False)
    rating = models.FloatField(blank=False, null=False, default=0.0)
    deleted = models.BooleanField(default=False)
