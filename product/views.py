from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework.response import Response
from .utlis import get_association_rules_recommendations

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# class ProductDetailView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
    

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

    
        recommendations = get_association_rules_recommendations(instance.id)
        recommendations_serializer = ProductSerializer(recommendations, many=True)

        data = serializer.data
        data['recommendations'] = recommendations_serializer.data

        return Response(data)




def index(request):
       products = Product.objects.all()
       return render(request, 'product/test.html', {'products':products })
    