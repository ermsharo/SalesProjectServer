from django.urls import path

from .views import ProductDetail, ProductList, SellerDetail, SellerList

urlpatterns = [
    path("product/", ProductList.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("seller/", SellerList.as_view(), name="seller_list"),
    path("seller/<int:pk>/", SellerDetail.as_view(), name="seller_detail"),
]
