from django.urls import path
from . import views


urlpatterns = [
    path('', views.FileUploaderView.as_view(), name="Uploader"),
    path('<path:file>', views.FileUploaderDetailAPIView.as_view(), name="Uploader"),

]