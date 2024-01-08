from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetailtView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



def index(request):
       products = Product.objects.all()
       return render(request, 'product/test.html', {'products':products })
    