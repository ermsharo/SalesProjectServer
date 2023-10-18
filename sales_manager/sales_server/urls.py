from django.urls import path

from .views import (
    ClientList,
    ClientDetail,
    ProductDetail,
    ProductList,
    SaleList,
    SaleDetail,
    SellerDetail,
    SellerList,
)

urlpatterns = [
    path("product/", ProductList.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("seller/", SellerList.as_view(), name="seller_list"),
    path("seller/<int:pk>/", SellerDetail.as_view(), name="seller_detail"),
    path("client/", ClientList.as_view(), name="client_list"),
    path("client/<int:pk>/", ClientDetail.as_view(), name="client_detail"),
    path("seller/", SellerList.as_view(), name="seller_list"),
    path("seller/<int:pk>/", SellerDetail.as_view(), name="seller_detail"),
    path("sale/", SaleList.as_view(), name="sale_list"),
    path("sale/<int:pk>/", SaleDetail.as_view(), name="sale_detail"),
]
