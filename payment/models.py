from django.db import models
from orders.models import Orders
from django.conf import settings
# Create your models here.
class Payment(models.Model):
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField(blank=False,null=False,default=None)
    comment=models.TextField(max_length=500,blank=True,null=True)
