from django.db import models

from suppliers.models import Suppliers


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Suppliers, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    def __str__(self):
        return self.name

