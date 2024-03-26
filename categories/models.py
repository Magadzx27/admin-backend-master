from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True, default=None)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
