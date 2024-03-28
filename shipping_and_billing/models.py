from django.db import models
from customers.models import User


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    ADDRESS_TYPE_CHOICES = [
        ('Shipping', 'Shipping'),
        ('Billing', 'Billing')
    ]
    address_type = models.CharField(max_length=8, choices=ADDRESS_TYPE_CHOICES)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"Address of the {self.user}"
