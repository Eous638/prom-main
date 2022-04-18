from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from prometheus import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'supercategories', views.SuperCategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
