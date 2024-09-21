from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to = "Image File")
    date = models.DateTimeField(auto_now_add = "true")

    def __str__(self):
        return str(self.id)