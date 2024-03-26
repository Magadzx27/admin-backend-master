from django.urls import path
from . import views


urlpatterns = [
    path('', views.PaymentAPIView.as_view(), name="Payment"),
    path('<int:id>', views.PaymentValueAPIView.as_view(), name="Payment"),
]