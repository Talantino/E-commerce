from django.urls import path, include
from rest_framework import routers
from .views import OrderItemViewSet, OrderDetailsViewSet


router = routers.SimpleRouter()
router.register(r'order-details', OrderDetailsViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
