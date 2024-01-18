from django.urls import path
from .views import send_reset_code,verify_reset_code

urlpatterns = [
    path('send_reset_code/', send_reset_code, name='send_reset_code'),
    path('verify_reset_code/', verify_reset_code, name='verify_reset_code'),

]