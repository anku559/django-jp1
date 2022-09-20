from django.urls import path
from . import views


# URL Configuration Module
urlpatterns = [
    path("test/", views.ProductRouteManager.as_view(), name="product"),
    path("product/", views.fetch_products, name="product"),
]
