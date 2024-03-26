from django.db import models
from newone import settings


# Create your models here.
class Aboutus(models.Model):
    key=models.CharField(max_length=255,blank=False,null=False, unique=True)
    value=models.CharField(max_length=1000,blank=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    