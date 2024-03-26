from django.db import models
from orders.models import Orders
from authentication.models import User
from django.conf import settings
# Create your models here.
class Shipping(models.Model):
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(max_length=1500,blank=True,null=True)
   
