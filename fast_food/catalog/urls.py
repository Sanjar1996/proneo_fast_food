from django.urls import path,include
from rest_framework import routers
from .views import catalog, api_category
from api.catalog.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

app_name='catalog'
urlpatterns = [
    path('', catalog, name='catalog'),
    # path('api/category/', api_category, name='catalog_api'),
    path('api/', include(router.urls)),
]
