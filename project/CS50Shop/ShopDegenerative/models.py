from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photo_main/%Y/%m/%d/")
    weight = models.FloatField()
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

# Create your models here.
