from django.db import models
from customers.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    stock_quantity = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)
    discount_flag = models.BooleanField()

    def __str__(self):
        return self.name, self.category


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.supplier_name


class ProductReview(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product review on {self.product}"
