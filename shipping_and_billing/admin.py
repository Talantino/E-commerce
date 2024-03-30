from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ("address_type", "street", "city", "state", "postal_code", "country", "user")


admin.site.register(Address, AddressAdmin)
