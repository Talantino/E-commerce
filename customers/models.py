from django.db import models
from django.contrib.auth.models import AbstractUser #PermissionsMixin


class User(AbstractUser):
    user_type_choices = [
        ('customer', 'customer'),
        ('supplier', 'supplier'),
        ('admin', 'admin'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(
        max_length=255,
        choices=user_type_choices,
        null=True,
        default='customer'
    )
    phone = models.CharField(max_length=255, unique=True, null=True)
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'user_type']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.email} - {self.last_name}"
