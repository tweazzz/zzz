# client/urls.py
from django.urls import path, include,re_path
from djoser.views import TokenCreateView
from auth_user.views import ClientUserCreateView,CustomTokenCreateView,CustomUserViewSet
from rest_framework.routers import DefaultRouter
from .views import *

client_router = DefaultRouter()
client_router.register(r'api/users', CustomUserViewSet, basename='client')
client_router.register(r'api/school', SchoolsApi,basename='api-school')
client_router.register(r'api/classroom', ClassroomApi,basename='api-classroom')
client_router.register(r'api/teacher', TeacherApi,basename='api-teacher')
client_router.register(r'api/class', ClassApi,basename='api-class')
client_router.register(r'api/schedule', ScheduleApi,basename='api-schedule')
client_router.register(r'api/menu', MenuApi,basename='api-menu')
client_router.register(r'api/slider', SliderApi,basename='api-slider')
client_router.register(r'api/subject', SubjectApi,basename='api-subject')
client_router.register(r'api/schoolpasport', schoolPasportApi,basename='api-schoolpasport')
client_router.register(r'api/school_administration', School_AdministrationApi,basename='api-school_administration')
client_router.register(r'api/school_director', School_DirectorApi,basename='api-school_director')
client_router.register(r'api/extra_lesson', Extra_LessonsApi,basename='api-extra_lesson')
client_router.register(r'api/kruzhok', KruzhokListApi,basename='api-kruzhok')
client_router.register(r'api/Sport_SuccessApi', Sport_SuccessApi,basename='api-Sport_SuccessApi')
client_router.register(r'api/Oner_SuccessApi', Oner_SuccessApi,basename='api-Oner_SuccessApi')
client_router.register(r'api/PandikOlimpiadaApi', PandikOlimpiadaApi,basename='api-PandikOlimpiadaApi')
client_router.register(r'api/School_RedCertificateApi', School_RedCertificateApi,basename='api-School_RedCertificateApi')
client_router.register(r'api/School_AltynBelgiApi', School_AltynBelgiApi,basename='api-School_AltynBelgiApi')
client_router.register(r'api/School_SocialMediaApi', School_SocialMediaApi,basename='api-School_SocialMediaApi')
client_router.register(r'api/ringApi', RingApi,basename='api-ringApi')
client_router.register(r'api/DopUrokApi', DopUrokApi,basename='api-DopUrokApi')
client_router.register(r'api/DopUrokRingApi', DopUrokRingApi,basename='api-DopUrokRingApi')
client_router.register(r'api/newsApi', NewsApi,basename='api-NewsApi')
client_router.register(r'api/notification', NotificationsApi,basename='api-notification')
client_router.register(r'api/schoolmap', SchoolMapApi,basename='api-schoolmap')


urlpatterns = [
    path('', include(client_router.urls)),
    path('login/', CustomTokenCreateView.as_view(), name='client_token_create'),
    path('register/', ClientUserCreateView.as_view(), name='client_user_create'),
]
