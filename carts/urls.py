from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartsAPIView.as_view(), name="Carts"),
    path('<int:id>', views.CartsDetailAPIView.as_view(), name="Carts")
    
] 