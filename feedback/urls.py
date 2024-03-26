from django.urls import path
from . import views


urlpatterns = [
    path('', views.SendFeedAPIView.as_view(), name="Carts"),
]