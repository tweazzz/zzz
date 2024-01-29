from django.urls import path,re_path
from .views import send_reset_code,verify_reset_code,reset_password
from .utils import activate

urlpatterns = [
    path('send_reset_code/', send_reset_code, name='send_reset_code'),
    path('verify_reset_code/', verify_reset_code, name='verify_reset_code'),
    path('reset_password/', reset_password, name='reset_password'),
    re_path(
        r'confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,100}-[0-9A-Za-z]{1,200})/$',
        activate,
        name='activate'
    ),
]