from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="AL ASEMAH STORE",
        default_version='v1.0.0',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@AICompuMall.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    # path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('products/', include('products.urls')),
    path('category/', include('categories.urls')),
    path('carts/', include('carts.urls')),
    path('imageslider/', include('imageSlider.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('review/', include('product_review.urls')),
    path('upload/', include('file_uploader.urls')),
    path('shipping_method/', include('shipping_method.urls')),
    path('shipping/', include('shipping.urls')),
    path('payment/', include('payment.urls')),
    path('payment_method/', include('payment_method.urls')),
    path('order/', include('orders.urls')),
    path('order_item/', include('order_item.urls')),
    path('feedback/', include('feedback.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
