from rest_framework import permissions


class IsSupplier(permissions.BasePermission):
    """
    Custom permission to only allow suppliers to create products.
    """

    def has_permission(self, request, view):
        if request == "POST":
            return request.user.is_authenticated and request.user.user_type == "supplier"
