from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("order/", views.create_order, name="create_order"),
    path("success/", views.order_success_page, name="order_success"),
    path("api/np/cities/", views.np_cities, name="np_cities"),
    path("api/np/warehouses/", views.np_warehouses, name="np_warehouses"),
    path("api/colors/", views.colors_json, name="colors_json"),
]
