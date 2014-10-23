from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer, CategorySerializer2


class CategoryList(generics.ListCreateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer