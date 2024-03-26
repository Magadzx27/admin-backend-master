from django.urls import path
from . import views


urlpatterns = [
    path('', views.ImagesliderAPIView.as_view(), name="Imageslider"),
    path('<int:id>', views.ImagesliderValueAPIView.as_view(), name="Imageslider")
]