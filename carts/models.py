from django.db import models
from products.models import Products
from authentication.models import User

# Create your models here.


class Carts(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(
        max_digits=5, decimal_places=0, blank=False, null=False)
    comment = models.CharField(max_length=1000, blank=True, null=True)

