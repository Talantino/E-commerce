from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets, permissions
from rest_framework.viewsets import GenericViewSet, mixins
from .models import Product, ProductReview, Category
from .permissions import IsSupplier
from .serializers import ProductSerializer, CategorySerializer, ProductReviewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSupplier,]

    def get_permissions(self):
        # view lists only
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]    # [permissions.IsAuthenticated]
        else:
            # For create, update, delete
            permission_classes = [IsSupplier]
        return [permission() for permission in permission_classes]


class ProductReviewViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser,]
