from django.shortcuts import render
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from django.views.generic.base import View
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from admin_app.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from admin_app.permissions import IsAdminSchool,IsSuperAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from admin_app.filters import *
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser


class SchoolsApi(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter
    http_method_names = ['get','head','options']

class ClassroomApi(viewsets.ModelViewSet):
    queryset = Classrooms.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Classrooms.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Classrooms.objects.all()
        return Classrooms.objects.all()

class ClassApi(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Class.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Class.objects.all()
        return Class.objects.all()

class ScheduleApi(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Schedule.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Schedule.objects.all()
        return Schedule.objects.all()
    
    @action(detail=False, methods=['get'])
    def available_ring(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                ring = Ring.objects.all()
            else:
                ring = Ring.objects.filter(school=self.request.user.school)

            ring_filter = AvailableRingFilter(request.GET, queryset=ring)
            serializer = AvailableRingSerializer(ring_filter.qs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'])
    def available_subject(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classroom = Subject.objects.all()
            else:
                classroom = Subject.objects.filter(school=self.request.user.school)

            serializer = AvailableSubjectSerializer(classroom, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class MenuApi(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuFilter
    http_method_names = ['get','head','options']


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Menu.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Menu.objects.all()
        return Menu.objects.all()


class SliderApi(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SliderFilter
    http_method_names = ['get','head','options']


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Slider.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Slider.objects.all()
        return Slider.objects.all()


class SubjectApi(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubjectFilter
    http_method_names = ['get','head','options']


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Subject.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Subject.objects.all()
        return Subject.objects.all()


class schoolPasportApi(viewsets.ModelViewSet):
    model = schoolPasport
    photo_field = 'photo'
    queryset = schoolPasport.objects.all()
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_PasportFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return schoolPasport.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else schoolPasport.objects.all()
        return schoolPasport.objects.all()


class School_AdministrationApi(viewsets.ModelViewSet):
    queryset = School_Administration.objects.all()
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_AdministrationFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return School_Administration.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_Administration.objects.all()
        return School_Administration.objects.all()


class Sport_SuccessApi(viewsets.ModelViewSet):
    queryset = Sport_Success.objects.all()
    serializer_class = Sport_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Sport_SuccessFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Sport_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Sport_Success.objects.all()
        return Sport_Success.objects.all()

    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all()
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            classes_filter = AvailableClassesFilter(request.GET, queryset=classes)
            serializer = AvailableClassesSerializer(classes_filter.qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class Oner_SuccessApi(viewsets.ModelViewSet):
    queryset = Oner_Success.objects.all()
    serializer_class = Oner_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oner_SuccessFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Oner_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Oner_Success.objects.all()
        return Oner_Success.objects.all()
    
    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all()
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            serializer = AvailableClassesSerializer(classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class PandikOlimpiadaApi(viewsets.ModelViewSet):
    queryset = PandikOlimpiada_Success.objects.all()
    serializer_class = PandikOlimpiada_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PandikOlimpiada_SuccessFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return PandikOlimpiada_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else PandikOlimpiada_Success.objects.all()
        return PandikOlimpiada_Success.objects.all()
    
    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all()
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            serializer = AvailableClassesSerializer(classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class School_RedCertificateApi(viewsets.ModelViewSet):
    queryset = RedCertificate.objects.all()
    serializer_class = RedCertificateSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RedCertificateFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return RedCertificate.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else RedCertificate.objects.all()
        return RedCertificate.objects.all()


class School_AltynBelgiApi(viewsets.ModelViewSet):
    queryset = AltynBelgi.objects.all()
    serializer_class = AltynBelgiSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AltynBelgiFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return AltynBelgi.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else AltynBelgi.objects.all()
        return AltynBelgi.objects.all()
    
class School_SocialMediaApi(viewsets.ModelViewSet):
    queryset = School_SocialMedia.objects.all()
    serializer_class = School_SocialMediaSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_SocialMediaFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return School_SocialMedia.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_SocialMedia.objects.all()
        return School_SocialMedia.objects.all()


class School_DirectorApi(viewsets.ModelViewSet):
    queryset = School_Director.objects.all()
    serializer_class = School_DirectorSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_DirectorFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return School_Director.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_Director.objects.all()
        return School_Director.objects.all()


class Extra_LessonsApi(viewsets.ModelViewSet):
    queryset = Extra_Lessons.objects.all()
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Extra_LessonsFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Extra_Lessons.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Extra_Lessons.objects.all()
        return Extra_Lessons.objects.all()

    @action(detail=False, methods=['get'])
    def available_typez(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                typez = Extra_Lessons.objects.all()
            else:
                typez = Extra_Lessons.objects.filter(school=self.request.user.school)

            serializer = Extra_LessonSerializer(typez, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class RingApi(viewsets.ModelViewSet):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RingFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Ring.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Ring.objects.all()
        return Ring.objects.all()



class TeacherApi(viewsets.ModelViewSet):
    model = Teacher
    photo_field = 'photo3x4'
    queryset = Teacher.objects.all()
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter
    http_method_names = ['get','head','options']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve','upload_photo']:
            return TeacherReadSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TeacherWriteSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            if self.request.user.school:
                serializer.validated_data['school'] = self.request.user.school
        serializer.save()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Teacher.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Teacher.objects.all()
        return Teacher.objects.all()

class TeacherWorkloadApi(viewsets.ModelViewSet):
    queryset = TeacherWorkload.objects.all()
    serializer_class = TeacherWorkloadSerializer
    permission_classes = [IsAdminSchool]
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return TeacherWorkload.objects.filter(school=self.request.user.school)




class KruzhokListApi(viewsets.ModelViewSet):
    model = Kruzhok
    photo_field = 'photo'
    queryset = Kruzhok.objects.all()
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = KruzhokFilter
    http_method_names = ['get','head','options']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve','upload_photo']:
            return KruzhokReadSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return KruzhokWriteSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Kruzhok.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Kruzhok.objects.all()
        return Kruzhok.objects.all()

    @action(detail=False, methods=['get'])
    def available_teachers(self, request, *args, **kwargs):
        teachers = Teacher.objects.filter(school=request.user.school)
        serializer = AvailableTeacherSerializer(teachers, many=True, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        lessons = instance.lessons.all()
        for lesson in lessons:
            lesson.delete()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)

class DopUrokApi(viewsets.ModelViewSet):
    queryset = DopUrok.objects.all()
    serializer_class = DopUrokSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return DopUrok.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else DopUrok.objects.all()
        return DopUrok.objects.all()


class DopUrokRingApi(viewsets.ModelViewSet):
    queryset = DopUrokRing.objects.all()
    serializer_class = DopUrokRingSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokRingFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return DopUrokRing.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else DopUrokRing.objects.all()
        return DopUrokRing.objects.all()

class NewsApi(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return News.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else News.objects.all()
        return News.objects.all()
    
class NotificationsApi(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAdminSchool]
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Notifications.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Notifications.objects.all()
        return Notifications.objects.all()
    
class SchoolMapApi(viewsets.ModelViewSet):
    queryset = SchoolMap.objects.all()
    serializer_class = SchoolMapSerializer
    permission_classes = [IsAdminSchool]
    http_method_names = ['get','head','options']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return SchoolMap.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else SchoolMap.objects.all()
        return SchoolMap.objects.all()
    

import pickle
from django.http import JsonResponse
from django.views import View
import os

class GetPostsDataView(View):
    def get(self, request, *args, **kwargs):
        pickle_directory = 'main'

        all_accounts_data = []

        try:
            for filename in os.listdir(pickle_directory):
                if filename.endswith('_data.pickle'):
                    pickle_file_path = os.path.join(pickle_directory, filename)

                    with open(pickle_file_path, 'rb') as pickle_in:
                        account_data = pickle.load(pickle_in)

                    all_accounts_data.extend(account_data)

            school_param = request.GET.get('school')
            account_name_param = request.GET.get('account_name')

            filtered_data = self.filter_data(all_accounts_data, school_param, account_name_param)

            return JsonResponse({'accounts_data': filtered_data})

        except FileNotFoundError:
            return JsonResponse({'error': 'File not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def filter_data(self, data, school_param, account_name_param):
        filtered_data = []

        for item in data:
            if school_param and item.get('school') is not None and item.get('school') != int(school_param):
                print(f"Skipping item {item['id']} due to school mismatch (expected {school_param}, got {item['school']})")
                continue

            if account_name_param and item.get('login') is not None and item.get('login') != account_name_param:
                print(f"Skipping item {item['id']} due to account name mismatch (expected {account_name_param}, got {item['login']})")
                continue

            post_data = {
                'id': item.get('id'),
                'text': item.get('text'),
                'timestamp': item.get('timestamp'),
                'media': [],
                'login': item.get('login') if item.get('login') is not None else 'N/A',
                'school': item.get('school') if item.get('school') is not None else 'N/A'
            }

            for media_item in item.get('media'):
                media_data = {
                    'url': media_item['url'],
                    'is_video': media_item['is_video']
                }

                # Добавление thumbnail_url для видео
                if media_item['is_video']:
                    media_data['thumbnail_url'] = media_item.get('thumbnail_url', 'N/A')

                post_data['media'].append(media_data)

            filtered_data.append(post_data)

        return filtered_data