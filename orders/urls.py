from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrdersAPIView.as_view(), name="Orders"),
    path('<int:id>', views.OrdersValueAPIView.as_view(), name="Orders"),
    path('checkout/', views.CheckoutAPIView.as_view(), name="Orders"),
]