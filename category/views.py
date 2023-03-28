from rest_framework import generics

from category.models import Category
from category.serializers import CategoryListSerializer


# Create your views here.
class CategoryListViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailViewSet(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryCreateViewSet(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryUpdateViewSet(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDeleteViewSet(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
