from rest_framework import serializers

from products.models import Order, OrderProduct
from products.serializers.order_product import OrderProductSerializer


# class OrderSerializer(serializers.ModelSerializer):
#     # user_id = serializers.IntegerField()
#     order_products = OrderProductSerializer(many=True)
#
#     class Meta:
#         model = Order
#         fields = ('id', 'user_id', 'order_products')
#
#
#     def create(self, validated_data):
#         order_products = validated_data.pop('order_products')
#         order = Order.objects.create(**validated_data)
#         for order_product in order_products:
#             OrderProduct.objects.create(order=order, **order_product)
#             # order.order_products.create(**order_product)
#         return order

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, source='orderproduct_set')

    class Meta:
        model = Order
        fields = ('id', 'user', 'order_products')

    def create(self, validated_data):
        order_products = validated_data.pop('order_products')
        order = Order.objects.create(**validated_data)
        for order_product_data in order_products:
            OrderProduct.objects.create(order=order, **order_product_data)
        return order
