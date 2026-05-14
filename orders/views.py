from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Order
from .serializers import OrderSerializer


@extend_schema(responses=OrderSerializer(many=True))
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_orders(request):
    orders = Order.objects.filter(user=request.user).select_related('product').order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
