from rest_framework import generics

from .models import Client_agent, Product, Sale, Seller_agent
from .serializers import (
    ClientSerializer,
    ProductSerializer,
    SaleSerializer,
    SellerSerializer,
)

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


class ClientList(generics.ListCreateAPIView):
    queryset = Client_agent.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client_agent.objects.all()
    serializer_class = ClientSerializer


class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
