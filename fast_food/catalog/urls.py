from django.urls import path,include
from .views import catalog, api_category




app_name='catalog'
urlpatterns = [
    path('', catalog, name='catalog'),
    # path('api/category/', api_category, name='catalog_api'),

]
