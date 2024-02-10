from rest_framework import serializers
from products.serializers.order_product import OrerProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField()
    order_products = OrerProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user_id', 'order_products')
