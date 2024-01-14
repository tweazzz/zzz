# client/urls.py
from django.urls import path, include,re_path
from djoser.views import TokenCreateView
from auth_user.views import ClientUserCreateView,CustomTokenCreateView
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'api/school', SchoolsApi)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomTokenCreateView.as_view(), name='client_token_create'),
    path('register/', ClientUserCreateView.as_view(), name='client_user_create'),
]
