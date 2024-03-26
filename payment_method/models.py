from django.db import models

# Create your models here.
class Payment_method(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    image_url=models.URLField(max_length=500,blank=True,null=True)
    info_message=models.CharField(max_length=1000,blank=True,null=True)
    deleted=models.BooleanField(default=False)