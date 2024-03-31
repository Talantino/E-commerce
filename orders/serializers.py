from .models import OrderDetails, OrderItem
from rest_framework import serializers
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price_at_purchase', 'get_total_price']
        read_only_fields = ['price_at_purchase', 'get_total_price']


class OrderDetailsSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = OrderDetails
        fields = ['id', 'user', 'order_date', 'shipping_address', 'billing_address', 'total_price', 'status', 'payment_method', 'discount_applied', 'order_items']
        read_only_fields = ['total_price', 'discount_applied']
