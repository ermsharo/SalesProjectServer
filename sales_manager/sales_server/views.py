from rest_framework import generics

from .models import Product, Seller_agent
from .serializers import ProductSerializer, SellerSerializer

# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SellerList(generics.ListCreateAPIView):
    queryset = Seller_agent.objects.all()
    serializer_class = SellerSerializer


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller_agent.objects.all()
    serializer_class = SellerSerializer
