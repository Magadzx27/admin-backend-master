from django.urls import path
from . import views


urlpatterns = [
    path('', views.Shipping_methodAPIView.as_view(), name="Shipping_method"),
    path('<int:id>', views.Shipping_methodDetailAPIView.as_view(), name="Shipping_method"),
]