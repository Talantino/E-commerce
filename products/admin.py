from django.contrib import admin
from .models import Product, ProductReview, Category

admin.site.register(Category)
admin.site.register(ProductReview)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock_quantity", "supplier")
