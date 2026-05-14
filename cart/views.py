from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer

from products.models import Product
from .models import Cart
from .serializers import CartSerializer


def get_user_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


cart_add_request = inline_serializer(
    name='CartAddRequest',
    fields={'productId': serializers.IntegerField()},
)


@extend_schema(responses=CartSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_detail(request):
    cart = get_user_cart(request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@extend_schema(request=cart_add_request, responses=CartSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_add(request):
    product_id = request.data.get('productId')
    if not product_id:
        return Response({'detail': 'productId is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    cart = get_user_cart(request.user)
    cart.products.add(product)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@extend_schema(responses=CartSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cart_remove(request, product_id):
    cart = get_user_cart(request.user)
    cart.products.remove(product_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data)
