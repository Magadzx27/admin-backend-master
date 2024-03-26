from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewAPIView.as_view(), name="Products"),
    path('<int:id>', views.ReviewDetailAPIView.as_view(), name="Products"),
]
