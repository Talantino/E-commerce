from .serializers import AddressSerializers
from rest_framework import viewsets
from .models import Address


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers
    permission_classes = []
