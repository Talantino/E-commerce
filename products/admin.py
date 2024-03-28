from django.contrib import admin
from .models import Product, ProductReview, Category, Supplier

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductReview)
admin.site.register(Supplier)
