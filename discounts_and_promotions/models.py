# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
# from products.models import Product
# # from django.core.exceptions import ValidationError
# # from django.utils import timezone
#
#
# class Discount(models.Model):
#     discount_rule = models.CharField(max_length=255)
#     threshold_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="discount")
#     discount_type = models.CharField(max_length=10, choices=[('percent', 'Percentage'), ('flat', 'Flat Rate')])
#     discount_percent = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         validators=[MinValueValidator(0), MaxValueValidator(100)]
#     )
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#
#     class Meta:
#         verbose_name = "Discount"
#         verbose_name_plural = "Discounts"
#
#     def __str__(self):
#         return f"{self.discount_type} discount for {self.product.name}"


# class PromoCode(models.Model):
#     code = models.CharField(max_length=255, unique=True)
#     discount_percent = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         validators=[MinValueValidator(0), MaxValueValidator(100)]
#     )
#     expiry_date = models.DateTimeField()
#     start_date = models.DateTimeField()
#     is_active = models.BooleanField(default=True)
#
#     def clean(self):
#         if self.start_date >= self.expiry_date:
#             raise ValidationError("End date must be after start date.")
#         super().clean()
#
#     class Meta:
#         verbose_name = "Promo-code"
#         verbose_name_plural = "Promo-codes"
#
#     def __str__(self):
#         return f"Promo code {self.code}"
#
#     def save(self, *args, **kwargs):
#         if self.expiry_date < timezone.now():
#             self.is_active = False
#         super().save(*args, **kwargs)
