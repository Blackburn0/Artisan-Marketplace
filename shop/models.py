from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(blank=False, max_length=6, choices=GENDER)
    address = models.CharField(blank=False, max_length=250)
    is_vendor = models.BooleanField(default=False)

# class Vendor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# class Product(model.Model):
#     name = models.CharField(max_length=250)
#     detail = models.TextField()
#     in_stock = models.IntegerField()
#     price = models.SmallIntegerField(max_length=8, )