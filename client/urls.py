# client/urls.py
from django.urls import path, include,re_path
from djoser.views import TokenCreateView
from auth_user.views import ClientUserCreateView,CustomTokenCreateView,CustomUserViewSet
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'api/users', CustomUserViewSet, basename='client')
router.register(r'api/school', SchoolsApi)
router.register(r'api/classroom', ClassroomApi)
router.register(r'api/teacher', TeacherApi)
router.register(r'api/class', ClassApi)
router.register(r'api/schedule', ScheduleApi)
router.register(r'api/menu', MenuApi)
router.register(r'api/slider', SliderApi)
router.register(r'api/subject', SubjectApi)
router.register(r'api/schoolpasport', schoolPasportApi)
router.register(r'api/school_administration', School_AdministrationApi)
router.register(r'api/school_director', School_DirectorApi)
router.register(r'api/extra_lesson', Extra_LessonsApi)
router.register(r'api/kruzhok', KruzhokListApi)
router.register(r'api/Sport_SuccessApi', Sport_SuccessApi)
router.register(r'api/Oner_SuccessApi', Oner_SuccessApi)
router.register(r'api/PandikOlimpiadaApi', PandikOlimpiadaApi)
router.register(r'api/School_RedCertificateApi', School_RedCertificateApi)
router.register(r'api/School_AltynBelgiApi', School_AltynBelgiApi)
router.register(r'api/School_SocialMediaApi', School_SocialMediaApi)
router.register(r'api/ringApi', RingApi)
router.register(r'api/DopUrokApi', DopUrokApi)
router.register(r'api/DopUrokRingApi', DopUrokRingApi)
router.register(r'api/newsApi', NewsApi)
router.register(r'api/notification', NotificationsApi)
router.register(r'api/schoolmap', SchoolMapApi)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomTokenCreateView.as_view(), name='client_token_create'),
    path('register/', ClientUserCreateView.as_view(), name='client_user_create'),
]
