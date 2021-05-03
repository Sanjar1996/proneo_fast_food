from rest_framework import serializers
from catalog.models import Category, Product


# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'sort_order']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
