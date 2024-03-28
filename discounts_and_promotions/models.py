from django.db import models
from products.models import Product


class Discount(models.Model):
    discount_rule = models.CharField(max_length=255)
    threshold_amount = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="discount")
    discount_type = models.CharField(max_length=10, choices=[('percent', 'Percentage'), ('flat', 'Flat Rate')])
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return f"{self.discount_type} discount for {self.product.name}"


class PromoCode(models.Model):
    code = models.CharField(max_length=255)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Promo-code"
        verbose_name_plural = "Promo-codes"

    def __str__(self):
        return f"Promo code {self.code}"
