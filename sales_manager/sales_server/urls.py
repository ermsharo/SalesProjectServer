from django.urls import path

from .views import ProductDetail, ProductList, SellerDetail, SellerList, Client_agent, Sale_agent

urlpatterns = [
    path("product/", ProductList.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("seller/", SellerList.as_view(), name="seller_list"),
    path("seller/<int:pk>/", SellerDetail.as_view(), name="seller_detail"),
    path("client/", Client_agent.as_view(), name="client_list"),
    path("client/<int:pk>/", Client_agent.as_view(), name="client_detail"),
    path("seller/", Client_agent.as_view(), name="seller_list"),
    path("seller/<int:pk>/", Client_agent.as_view(), name="seller_detail"),
    path("sale/", Sale_agent.as_view(), name="sale_list"),
    path("sale/<int:pk>/", Sale_agent.as_view(), name="sale_detail"),
]
