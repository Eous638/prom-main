from rest_framework import serializers
from .models import Product, Category, SuperCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'image', 'category')
        
class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('title', 'image',  'product')

class SuperCategorySerializer(serializers.ModelSerializer):
    category =  CategorySerializer(many=True, read_only=True)
    class Meta:
        model = SuperCategory
        fields = ['title',  'image', 'category','id_field']