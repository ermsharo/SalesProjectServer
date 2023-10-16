from rest_framework import serializers

from .models import Product, Sale, Seller_agent


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_agent
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"
