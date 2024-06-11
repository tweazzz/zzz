from django.urls import path, include,re_path
from admin_app.views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import TokenCreateView
from auth_user.views import AdminUserCreateView,CustomTokenCreateView ,AdminUserViewSet, UserMeView
# from autogenerate.views import AutoSchedulerView,GenerateSubjectView


admin_router = DefaultRouter()
# router.register(r'api/admin', AdminsApi)
admin_router.register(r'users', AdminUserViewSet, basename='admin')
admin_router.register(r'schools', SchoolsApi)
admin_router.register(r'classrooms', ClassroomApi)
admin_router.register(r'teachers', TeacherApi,basename='teacher')
admin_router.register(r'classes', ClassApi, basename='class')
admin_router.register(r'schedules', ScheduleApi)
admin_router.register(r'foodmenu', MenuApi)
admin_router.register(r'sliders', SliderApi)
admin_router.register(r'subjects', SubjectApi)
admin_router.register(r'schoolpasport', schoolPasportApi)
admin_router.register(r'schooladmins', School_AdministrationApi)
admin_router.register(r'api/school_director', School_DirectorApi)
admin_router.register(r'api/extra_lesson', Extra_LessonsApi)
admin_router.register(r'api/kruzhok', KruzhokListApi, basename='kruzhok')
admin_router.register(r'api/Sport_SuccessApi', Sport_SuccessApi)
admin_router.register(r'api/Oner_SuccessApi', Oner_SuccessApi)
admin_router.register(r'api/PandikOlimpiadaApi', PandikOlimpiadaApi)
admin_router.register(r'api/School_RedCertificateApi', School_RedCertificateApi)
admin_router.register(r'api/School_AltynBelgiApi', School_AltynBelgiApi)
admin_router.register(r'api/School_SocialMediaApi', School_SocialMediaApi)
admin_router.register(r'api/ringApi', RingApi)
admin_router.register(r'api/DopUrokApi', DopUrokApi)
admin_router.register(r'api/DopUrokRingApi', DopUrokRingApi)
admin_router.register(r'api/newsApi', NewsApi, basename='news')
admin_router.register(r'api/notification', NotificationsApi)
admin_router.register(r'api/schoolmap', SchoolMapApi)
admin_router.register(r'api/main_slider', MainSchoolPhotoView,basename='main_slider')
admin_router.register(r'api/map_coordinates', MapCoordinatesView ,basename='map_coordinates')
admin_router.register(r'api/proudofschool', ProudOfSchoolView ,basename='proud_of_school')

urlpatterns = [
    path('', include(admin_router.urls)),
    path('login/', CustomTokenCreateView.as_view(), name='admin_token_create'),
    path('register/', AdminUserCreateView.as_view(), name='admin_create'),
    path('api/available_school/', SchoolsApi.as_view({'get': 'available_school'}), name='available-school'),
    path('api/available_teachers/', KruzhokListApi.as_view({'get': 'available_teachers'}), name='available_teachers'),
    path('api/available_classes/', ClassApi.as_view({'get': 'available_classes'}), name='available_classes'),
    path('api/available_classrooms/', ClassroomApi.as_view({'get': 'available_classrooms'}), name='available_classrooms'),
    path('api/available_ring/', ScheduleApi.as_view({'get': 'available_ring'}), name='available-ring'),
    path('api/available_dopurok_ring/', ScheduleApi.as_view({'get': 'available_dopurok_ring'}), name='available_dopurok_ring-ring'),
    path('api/available_subject/', ScheduleApi.as_view({'get': 'available_subject'}), name='available-subject'),
    path('api/available_typez/', Extra_LessonsApi.as_view({'get': 'available_typez'}), name='available-typez'),
    path('api/kruzhok/upload_photo/', KruzhokListApi.as_view({'post': 'upload_photo'}), name='upload_photo'),
    path('api/teacher/upload_photo/', TeacherApi.as_view({'post': 'upload_photo'}), name='upload_photo'),
    path('api/schoolpasport/upload_photo/', schoolPasportApi.as_view({'post': 'upload_photo'}), name='upload_photo'),
    path('users/me/', UserMeView.as_view(), name='user-me'),
    path('get_posts_data/', GetPostsDataView.as_view(), name='get_posts_data'),
    # path('create_schedule/', AutoSchedulerView.as_view(), name='auto-schedule'),
    # path('auto_generate/', GenerateSubjectView.as_view(), name='auto-copy'),
    path('api/delete_class_schedule/', ScheduleApi.as_view({'post': 'delete_schedule_by_class'}), name='delete-class-schedule'),
    path('api/delete_class_dopurok/', DopUrokApi.as_view({'post': 'delete_schedule_by_class'}), name='delete-class-dopurok'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)