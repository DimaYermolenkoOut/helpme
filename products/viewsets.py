from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import products
from products.models import Product, Category, Tag
from products.serializers import ProductSerializer, CategorySerializer, TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # отримання суми цін по категоріях
    @action(detail=True, methods=['get'])
    def get_sum_by_category(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        if products.exists():
            sum_by_category = products.aggregate(Sum('price'))['price__sum']
            return Response({'sum_by_category': sum_by_category})
        else:
            return Response({'sum_by_category': 0})


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


