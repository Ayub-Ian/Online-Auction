from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="products")
    description = models.TextField(max_length=500, blank=True)
    reserve_price = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Bid(models.Model):
    bid_value = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} : bid {self.bid_value} on {self.product.name} at {self.date}"
