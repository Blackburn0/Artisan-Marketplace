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
    profile_image = models.ImageField(upload_to="User_profile_images", blank=True, null=True)
    address = models.CharField(max_length=250)
    is_vendor = models.BooleanField(default=False)

class Vendor(models.Model):

    vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name
    # phone_number = models.IntegerField()
    # business_certificate_image = models.ImageField(upload_to="Vendeor_Business_Certificate", blank=True)
    # business_name = models.CharField( max_length=100)

    # profile_image = models.ImageField(upload_to="Vendor_profile_images", blank=True, null=True)
    # gender = models.CharField(blank=False, max_length=6, choices=GENDER)
    # address = models.CharField(max_length=250)
    # phone_number = models.IntegerField()


# class Product(model.Model):
#     name = models.CharField(max_length=250)
#     detail = models.TextField()
#     in_stock = models.IntegerField()
#     price = models.SmallIntegerField(max_length=8, )