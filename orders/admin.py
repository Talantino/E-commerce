from django.contrib import admin
from .models import OrderItem, OrderDetails
from products.models import Product


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ("shipping_address", "total_price", "status", "payment_method", "discount_applied")


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price_at_purchase', 'get_total_price']
    readonly_fields = ['get_total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'

    def get_list_display(self, request):
        return self.list_display


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)

