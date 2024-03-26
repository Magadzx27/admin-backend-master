from django.db import models
from authentication.models import User
from products.models import Products
from orders.models import Orders
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.
class Orders_item(models.Model):
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=False,null=False)
    comment=models.TextField(max_length=1500,blank=True,null=True)
    