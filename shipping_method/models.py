from django.db import models
# Create your models here.
class Shipping_method(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    image_url=models.URLField(max_length=500,blank=True,null=True)
    contact_number=models.CharField(max_length=50,blank=True,null=True)
    info_message=models.CharField(max_length=1500,blank=True,null=True)
    price=models.FloatField(blank=False,null=True,default=None)
    deleted=models.BooleanField(default=False)
