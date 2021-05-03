from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
# from api.catalog.views import CategoryViewSet, ProductViewSet


# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)
# router.register(r'product', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('api/', include('api.urls')),
    path('', include('catalog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
