from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

# from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation for online store",
      default_version='v1',
      description="API documentation for E-commerce project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/customers/', include('customers.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('api/docs/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
