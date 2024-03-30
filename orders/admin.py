from django.contrib import admin
from .models import Order, OrderDetails


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ("shipping_address", "total_price", "status", "payment_method", "discount_applied")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
