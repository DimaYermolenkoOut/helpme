from django.contrib.auth.models import User
from django.db import models

from products.models.product import Product


class Order(models.Model):
    ''' замовлення клієнта '''
    # user наслідуємо з Django.contrib.auth.models
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # щоб Order  працював треба through таблиця/модель OrderProduct
    products = models.ManyToManyField(Product, related_name='products', through='OrderProduct')