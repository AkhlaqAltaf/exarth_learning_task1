from django.db import models


# Create your models here.
class PhotoModel(models.Model):
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo {self.id}'
