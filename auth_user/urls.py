from django.urls import path,re_path,include
from .views import send_reset_code,verify_reset_code,reset_password,send_verification_code,confirm_verification_code
from rest_framework.routers import DefaultRouter
from .views import FCMDeviceViewSet



router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send_reset_code/', send_reset_code, name='send_reset_code'),
    path('verify_reset_code/', verify_reset_code, name='verify_reset_code'),
    path('reset_password/', reset_password, name='reset_password'),
    path('verify_code/', send_verification_code, name='send_verification_code'),
    path('confirm_code/',confirm_verification_code,name='confirm_verification_code')
]