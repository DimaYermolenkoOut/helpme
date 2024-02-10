from django.db import models

from products.models.tag import Tag
from products.models.category import Category


class Product(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    summary = models.CharField(max_length=255)
    featured = models.BooleanField()
    is_18_plus = models.BooleanField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # якщо неправильно вказати related_name міграція не працюватиме
    orders = models.ManyToManyField('Order', through='OrderProduct', related_name='orders')

    def __str__(self):
        return f"{self.tittle} - {self.price}"