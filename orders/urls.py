from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet, OrderDetailsViewSet


router = DefaultRouter()
router.register(r'order-details', OrderDetailsViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
