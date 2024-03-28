from django.db import models


class Discount(models.Model):
    discount_rule = models.CharField(max_length=255)
    threshold_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return self.discount_rule


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
