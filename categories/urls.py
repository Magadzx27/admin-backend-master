from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoriesAPIView.as_view(), name="Categories"),
    path('<int:id>', views.CategoriesDetailAPIView.as_view(), name="Categories")
]
