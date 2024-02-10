from rest_framework import serializers


class OrerProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.FloatField(min_value=1)