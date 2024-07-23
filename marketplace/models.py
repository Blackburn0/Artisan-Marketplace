from itertools import product
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORIES = (
        ('shoe', 'Shoe'),
        ('clothe', 'Clothe'),
        ('cap', 'Cap'),
        ('belt', 'Belt')
    )
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='product_pictures/')
    detail = models.TextField()
    available_quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    
