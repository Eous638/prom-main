from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category, SuperCategory
from .serializers import ProductSerializer, CategorySerializer, SuperCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SuperCategoryViewSet(viewsets.ModelViewSet):
    queryset = SuperCategory.objects.all()
    serializer_class = SuperCategorySerializer