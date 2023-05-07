from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, blank=True)
    category = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    price_for_view = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)

    def __str__(self):
        return self.name


class Basket(models.Model):
    customer_id = models.IntegerField(blank=True,null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина : {self.product.name}'
