
from django.contrib import admin
from .models import Product, Category, SuperCategory
# Register your models here.

class CategoryInline(admin.TabularInline):
    model = Product.category.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',  'description', 'image')
    inlines = [CategoryInline]
         

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','supercategory', 'image')
    inlines = [CategoryInline]
    
    
    
@admin.register(SuperCategory)
class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image' )
    
    


