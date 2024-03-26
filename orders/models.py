from django.db import models
from django.contrib.auth.models import User
from payment_method.models import Payment_method
from shipping_method.models import Shipping_method
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.


class Orders(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shipping_id = models.ForeignKey(Shipping_method, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(
        Payment_method, on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(max_length=1000, blank=True, null=True)
    user_address = models.CharField(max_length=2000, blank=True, null=True)
    user_phone = PhoneNumberField()
    date = models.DateTimeField(auto_now_add=True)
    store_status = models.TextField(max_length=1500, blank=True, null=True)
    user_status = models.TextField(max_length=1500, blank=True, null=True)
    total = models.FloatField(blank=False, null=False, default=None)
