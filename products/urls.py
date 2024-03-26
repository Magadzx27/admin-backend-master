from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductsAPIView.as_view(), name="Products"),
    path('<int:id>', views.ProductsDetailAPIView.as_view(), name="Products"),
    path('test/<int:id>', views.ProductsTest.as_view(), name="Products")
]