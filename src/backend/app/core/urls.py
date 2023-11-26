from core.views import get_health
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", include("products.urls"), name="products"),
    path("api/health/", get_health, name="health"),
]
