from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     description = models.CharField(max_length=200)
#     photo_main = models.ImageField(upload_to="photo_main/%Y/%m/%d/")
#     photos = models.ImageField(upload_to="photo/%Y/%m/%d/")
#     category = models.CharField(max_length=255)
#     subcategory = models.CharField(max_length=255)
#     weight = models.FloatField()
#     price = models.FloatField()
#     stock = models.IntegerField()
#     available = models.BooleanField(default=True)


# class Registration(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)


# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)




# Create your models here.
