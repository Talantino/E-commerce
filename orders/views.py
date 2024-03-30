from rest_framework import viewsets
from .models import OrderItem, OrderDetails
from .serializers import OrderDetailsSerializer, OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = []


class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    permission_classes = []
