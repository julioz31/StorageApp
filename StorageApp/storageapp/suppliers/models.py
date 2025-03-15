from django.db import models

class Suppliers(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, default='SOME STRING')
    po_batkovi = models.CharField(max_length=255, default='SOME STRING')
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name } - {self.surname} - {self.po_batkovi}"

class SupplierProduct(models.Model):
    supplier = models.ForeignKey('suppliers.Suppliers', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    def get_product(self):
        Product = apps.get_model('products', 'Product')
        return Product.objects.get(id=self.product.id)
    def __str__(self):
        return f"{self.supplier.name} - {self.product.name}"