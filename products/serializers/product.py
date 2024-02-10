from rest_framework import serializers

from products.models import Product, Category, Tag

class ProductSerializer(serializers.ModelSerializer):
    price_usd = serializers.SerializerMethodField()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    def get_price_usd(self, obj):
        price_usd = obj.price / 38
        return round(price_usd, 2)



    class Meta:
        model = Product
        fields = ('id','tittle', 'description', 'price', 'summary', 'is_18_plus', 'featured', 'price_usd', 'category', 'tags')