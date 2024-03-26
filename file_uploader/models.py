from django.db import models
from PIL import Image

# Create your models here.


class UploderModel(models.Model):
    file = models.FileField(upload_to='uploaded_files/',
                            blank=False, null=False)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        super(UploderModel, self).save(*args, **kwargs)
        image = Image.open(self.file.path)
        image = image.convert('RGB')
        image.save(self.file.path, 'webp', quality=50, optimize=True)
        return self
