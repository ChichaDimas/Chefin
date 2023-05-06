from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128,blank=True)
    category = models.CharField(max_length=128,blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)


    def __str__(self):
        return self.name