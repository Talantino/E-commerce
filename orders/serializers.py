from .models import OrderDetails, OrderItem
from rest_framework import serializers


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = "__all__"
