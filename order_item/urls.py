from django.urls import path
from . import views


urlpatterns = [
    path('', views.Orders_itemAPIView.as_view(), name="Orders_item"),
    path('<int:id>', views.Orders_itemValueAPIView.as_view(), name="Orders_item"),
]