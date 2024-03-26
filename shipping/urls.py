from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShippingsAPIView.as_view(), name="Shipping_name"),
    path('<int:id>', views.ShippingsDetailAPIView.as_view(), name="Shipping_name"),
]