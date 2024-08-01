from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

class Customer(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER)
    profile_image = models.ImageField(upload_to='Customer_Profile')

    def __str__(self):
        return self.first_name

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField(blank=True)

    def __str__(self):
        return self.company_name
