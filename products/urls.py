from django.urls import path, include
from .views import ProductReviewViewSet, ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet) #basename ?
router.register(r'product-reviews', ProductReviewViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
