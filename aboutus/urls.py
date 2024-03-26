from django.urls import path
from . import views


urlpatterns = [
    path('', views.AboutusAPIView.as_view(), name="Aboutus"),
    path('<str:key>', views.AboutusValueAPIView.as_view(), name="Aboutus")
]