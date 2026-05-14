from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'product', 'created_at')
