from django.db import models

class Imageslider(models.Model):
    image_url=models.URLField(max_length=1000,blank=False,null=True)
    title=models.TextField(max_length=100,blank=True,null=True)
    subtitle=models.TextField(max_length=100,blank=True,null=True)
    display_order=models.IntegerField(blank=True,null=True, default=0)

    def __str__(self):
      return self.id