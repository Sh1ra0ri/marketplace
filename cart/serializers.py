from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='user_id', read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('userId', 'products')
