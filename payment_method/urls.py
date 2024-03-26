from django.urls import path
from . import views


urlpatterns = [
    path('', views.Payment_methodAPIView.as_view(), name="Payment_method"),
    path('<int:id>', views.Payment_methodDetailAPIView.as_view(), name="Payment_method"),
]