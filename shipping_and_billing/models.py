from django.db import models
# from customers.models import User
from django.conf import settings
from django.core.validators import RegexValidator


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="addresses", on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex='^\d{5}(-\d{4})?$',
                message='Postal code must be in the format XXXXX or XXXXX-XXXX.'
            )
        ]
    )
    country = models.CharField(max_length=255)
    ADDRESS_TYPE_CHOICES = [
        ('Shipping', 'Shipping'),
        ('Billing', 'Billing')
    ]
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.user} {self.address_type} address"

    def formatted_address(self):
        """Returns a multi-line string representation of the address."""
        return f"{self.street}\n{self.city}, {self.state} {self.postal_code}\n{self.country}"
