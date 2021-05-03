from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from catalog.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ListCategories(generics.ListAPIView, generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes  = [JSONParser, FormParser]


class OneCategories(generics.RetrieveAPIView,
                    generics.UpdateAPIView, generics.DestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_fields = ['id']

    def get_object(self):
        print( self.kwargs['id'])
        obj = get_object_or_404(Category, id=self.kwargs['id'])
        return obj


# class ListCategories(APIView):
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         categories = [category.name for category in Category.objects.all()]
#
#         return Response(categories)
#
#     def post(self, request, format=None):
#
#         return Response({'success': 'OK'})



# ViewSets define the view behavior.
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
