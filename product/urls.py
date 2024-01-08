from django.urls import path
from .views import ProductListView,ProductDetailtView,index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailtView.as_view(), name='product-detail'),
    path('test/', index, name='product'),
]

