from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from decimal import Decimal


# class Product(models.Model):
#     name = models.CharField(max_length=128, blank=True)
#     category = models.CharField(max_length=128, blank=True)
#     description = models.TextField(null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
#     price_for_view = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
#     image = models.ImageField(upload_to='products_images', blank=True)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, blank=True)
    category = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    price_for_view = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            # преобразование поля price в строку
        }

    def __str__(self):
        return self.name

class Basket(models.Model):
    customer_id = models.IntegerField(blank=True,null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина : {self.product.name}'

    def sum(self):
        return int(self.product.price_for_view) * self.quantity


# class BasketQuerySet(models.QuerySet):
#     def total_sum(self):
#         return sum(basket.sum() for basket in self)
#
#     def total_quantity(self):
#         return sum(basket.quantity for basket in self)