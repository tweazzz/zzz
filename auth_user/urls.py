from django.urls import path,re_path
from .views import send_reset_code,verify_reset_code,reset_password


urlpatterns = [
    path('send_reset_code/', send_reset_code, name='send_reset_code'),
    path('verify_reset_code/', verify_reset_code, name='verify_reset_code'),
    path('reset_password/', reset_password, name='reset_password'),
]