from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .yasg import urlpatterns as doc_urls
from django.urls import path, include, re_path

schema_view = get_schema_view(
    openapi.Info(
        title='sfootball api',
        description='This is sfootball api',
        default_version='v1',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='hamidullonematullayev22@gmail.com'),
        license=openapi.License(name="sfootball.uz"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('accounts.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('std/',include('stadium.urls')),
    path('bot_user/',include('bot_user.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ doc_urls
# urlpatterns
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


