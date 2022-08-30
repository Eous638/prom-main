from rest_framework import serializers
from .models import Product, Category, SuperCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'image', 'category', 'id_field')
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookp_field':'title'}
        }
        
class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('title', 'image',  'product')
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookp_field':'title'}
        }

class SuperCategorySerializer(serializers.ModelSerializer):
    category =  CategorySerializer(many=True, read_only=True)
    class Meta:
        model = SuperCategory
        fields = ['title',  'image', 'category','id_field']
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookp_field':'title'}
        }