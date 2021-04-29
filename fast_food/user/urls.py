from django.urls import path
from .views import sign, index

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('register/', sign, name='register'),
]
