from django.urls import path
from api.catalog.views import ListCategories, OneCategories

urlpatterns = [
    path('category/', ListCategories.as_view()),
    path('category/<int:id>/', OneCategories.as_view()),
]
