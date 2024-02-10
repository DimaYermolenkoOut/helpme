from django.contrib import admin

from products.models import Product, Category, Tag, Order


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'price']
    list_filter = ['price', 'is_18_plus', 'category', 'tags']
    search_fields = ['tittle', 'description', 'price']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']


