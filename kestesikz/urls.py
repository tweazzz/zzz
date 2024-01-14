from django.contrib import admin
from django.urls import path, include,re_path
from djoser.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_user.urls')),
    path('admins/', include('admin_app.urls')),
    path('client/', include('client.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]