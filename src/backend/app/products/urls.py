from django.urls import path
from products.views import get_products

urlpatterns = [
    path("", get_products, name="products"),
]
