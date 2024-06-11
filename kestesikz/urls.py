from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_user/', include('auth_user.urls')),
    path('admins/', include('admin_app.urls')),
    path('client/', include('client.urls')),
    path('auth/', include('djoser.urls')),
    path('api/v1/', include('generate_schedule.urls')),
    path('api/v1/', include('instagram_parsing.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path("__debug__/", include("debug_toolbar.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
