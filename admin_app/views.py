from django.shortcuts import render
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from django.views.generic.base import View
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminSchool,IsSuperAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser


class PhotoUploadMixin(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    model = None
    photo_field = None
    
    @action(detail=False, methods=['post','put'])
    def upload_photo(self, request, *args, **kwargs):
        obj_id = request.data.get('id')
        obj = get_object_or_404(self.model, id=obj_id)
        setattr(obj, self.photo_field, request.data.get(self.photo_field))
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

class SchoolsApi(viewsets.ModelViewSet):
    queryset = School.objects.select_related('user').order_by('id')
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter

    @action(detail=False, methods=['get'])
    def available_school(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            school = School.objects.select_related('user').order_by('id')
            serializer = AvailableSchoolSerializer(school, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

class ClassroomApi(viewsets.ModelViewSet):
    queryset = Classrooms.objects.all().select_related('school')
    serializer_class = ClassroomSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Classrooms.objects.all().select_related('school')
            if not self.request.user.is_superuser:
                queryset = queryset.filter(school=self.request.user.school)
            return queryset
        return Classrooms.objects.all().select_related('school')

    @action(detail=False, methods=['get'])
    def available_classrooms(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classroom = Classrooms.objects.select_related('school')
            else:
                classroom = Classrooms.objects.filter(school=self.request.user.school)

            serializer = AvailableClassRoomSerializer(classroom, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

class ClassApi(viewsets.ModelViewSet):
    queryset = Class.objects.all().select_related('school', 'classroom', 'class_teacher')
    serializer_class = ClassSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(school=self.request.user.school) if not self.request.user.is_superuser else self.queryset
        return self.queryset
    
    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all().select_related('school', 'classroom', 'class_teacher')
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            classes_filter = AvailableClassesFilter(request.GET, queryset=classes)
            serializer = AvailableClassesSerializer(classes_filter.qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

class ScheduleApi(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter

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
    def available_dopurok_ring(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                ring = DopUrokRing.objects.all()
            else:
                ring = DopUrokRing.objects.filter(school=self.request.user.school)

            ring_filter = AvailableDopUrokRingFilter(request.GET, queryset=ring)
            serializer = AvailableDopUrokRingSerializer(ring_filter.qs, many=True)

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
    queryset = Menu.objects.all().select_related('school')
    serializer_class = MenuSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuFilter


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Menu.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Menu.objects.all().select_related('school')
        return Menu.objects.all().select_related('school')

class SliderApi(viewsets.ModelViewSet):
    queryset = Slider.objects.all().select_related('school')
    serializer_class = SliderSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SliderFilter


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Slider.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Slider.objects.all().select_related('school')
        return Slider.objects.all().select_related('school')

class SubjectApi(viewsets.ModelViewSet):
    queryset = Subject.objects.all().select_related('school')
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubjectFilter


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Subject.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Subject.objects.all().select_related('school')
        return Subject.objects.all().select_related('school')

class schoolPasportApi(PhotoUploadMixin,viewsets.ModelViewSet):
    model = schoolPasport
    photo_field = 'photo'
    queryset = schoolPasport.objects.all().select_related('school')
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_PasportFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return schoolPasport.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else schoolPasport.objects.all().select_related('school')
        return schoolPasport.objects.all().select_related('school')

class School_AdministrationApi(viewsets.ModelViewSet):
    queryset = School_Administration.objects.all().select_related('school')
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_AdministrationFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return School_Administration.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_Administration.objects.all().select_related('school')
        return School_Administration.objects.all().select_related('school')

class Sport_SuccessApi(viewsets.ModelViewSet):
    queryset = Sport_Success.objects.all().select_related('school')
    serializer_class = Sport_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Sport_SuccessFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Sport_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Sport_Success.objects.all().select_related('school')
        return Sport_Success.objects.all().select_related('school')

class Oner_SuccessApi(viewsets.ModelViewSet):
    queryset = Oner_Success.objects.all().select_related('school')
    serializer_class = Oner_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oner_SuccessFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Oner_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Oner_Success.objects.all().select_related('school')
        return Oner_Success.objects.all().select_related('school')
    
class PandikOlimpiadaApi(viewsets.ModelViewSet):
    queryset = PandikOlimpiada_Success.objects.all().select_related('school')
    serializer_class = PandikOlimpiada_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PandikOlimpiada_SuccessFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return PandikOlimpiada_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else PandikOlimpiada_Success.objects.all().select_related('school')
        return PandikOlimpiada_Success.objects.all().select_related('school')

class School_RedCertificateApi(viewsets.ModelViewSet):
    queryset = RedCertificate.objects.all().select_related('school')
    serializer_class = RedCertificateSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RedCertificateFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return RedCertificate.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else RedCertificate.objects.all().select_related('school')
        return RedCertificate.objects.all().select_related('school')

class School_AltynBelgiApi(viewsets.ModelViewSet):
    queryset = AltynBelgi.objects.all().select_related('school')
    serializer_class = AltynBelgiSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AltynBelgiFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return AltynBelgi.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else AltynBelgi.objects.all().select_related('school')
        return AltynBelgi.objects.all().select_related('school')
    
class School_SocialMediaApi(viewsets.ModelViewSet):
    queryset = School_SocialMedia.objects.all().select_related('school')
    serializer_class = School_SocialMediaSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_SocialMediaFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return School_SocialMedia.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_SocialMedia.objects.all().select_related('school')
        return School_SocialMedia.objects.all().select_related('school')

class School_DirectorApi(viewsets.ModelViewSet):
    queryset = School_Director.objects.all().select_related('school')
    serializer_class = School_DirectorSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_DirectorFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return School_Director.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_Director.objects.all().select_related('school')
        return School_Director.objects.all().select_related('school')

class Extra_LessonsApi(viewsets.ModelViewSet):
    queryset = Extra_Lessons.objects.all().select_related('school')
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Extra_LessonsFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Extra_Lessons.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Extra_Lessons.objects.all().select_related('school')
        return Extra_Lessons.objects.all().select_related('school')

    @action(detail=False, methods=['get'])
    def available_typez(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                typez = Extra_Lessons.objects.all().select_related('school')
            else:
                typez = Extra_Lessons.objects.filter(school=self.request.user.school)

            serializer = Extra_LessonSerializer(typez, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

class RingApi(viewsets.ModelViewSet):
    queryset = Ring.objects.all().select_related('school')
    serializer_class = RingSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RingFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Ring.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Ring.objects.all().select_related('school')
        return Ring.objects.all().select_related('school')

from django.db.models import Prefetch
class TeacherApi(PhotoUploadMixin, viewsets.ModelViewSet):
    model = Teacher
    photo_field = 'photo3x4'
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

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
        queryset = Teacher.objects.all()
        
        # Оптимизация выборки данных из связанных таблиц
        queryset = queryset.select_related('school').prefetch_related(
            Prefetch('jobhistory_set', queryset=JobHistory.objects.select_related('teacher')),
            Prefetch('specialityhistory_set', queryset=SpecialityHistory.objects.select_related('teacher'))
        )
        
        # Оптимизация фильтрации данных
        if self.request.user.is_authenticated:
            queryset = queryset.filter(school=self.request.user.school) if not self.request.user.is_superuser else queryset

        return queryset

class TeacherWorkloadApi(viewsets.ModelViewSet):
    queryset = TeacherWorkload.objects.all()
    serializer_class = TeacherWorkloadSerializer
    permission_classes = [IsAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return TeacherWorkload.objects.filter(school=self.request.user.school)

class KruzhokListApi(PhotoUploadMixin, viewsets.ModelViewSet):
    model = Kruzhok
    photo_field = 'photo'
    queryset = Kruzhok.objects.all()
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    # filterset_class = KruzhokFilter

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
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(school=self.request.user.school) if not self.request.user.is_superuser else queryset

        queryset = queryset.prefetch_related('teacher', 'lessons')
        return queryset

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

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return DopUrokRing.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else DopUrokRing.objects.all()
        return DopUrokRing.objects.all()

class NewsApi(viewsets.ModelViewSet):
    queryset = News.objects.all().select_related('school')
    serializer_class = NewsSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return News.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else News.objects.all().select_related('school')
        return News.objects.all().select_related('school')
    
class NotificationsApi(viewsets.ModelViewSet):
    queryset = Notifications.objects.all().select_related('school')
    serializer_class = NotificationsSerializer
    permission_classes = [IsAdminSchool]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Notifications.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Notifications.objects.all().select_related('school')
        return Notifications.objects.all().select_related('school')
    
class SchoolMapApi(viewsets.ModelViewSet):
    queryset = SchoolMap.objects.all().select_related('school')
    serializer_class = SchoolMapSerializer
    permission_classes = [IsAdminSchool]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return SchoolMap.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else SchoolMap.objects.all().select_related('school')
        return SchoolMap.objects.all().select_related('school')
    
import pickle
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
import os

class GetPostsDataView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            pickle_file_path = 'C:/Users/dg078/Desktop/asdd/zzz/instaparser/common_instagram_data.pickle'

            with open(pickle_file_path, 'rb') as pickle_file:
                data = pickle.load(pickle_file)

            school_param = self.request.GET.get('school')
            account_name_param = self.request.GET.get('account_name')

            filtered_data = self.filter_data(data, school_param, account_name_param)

            return Response({'accounts_data': filtered_data})

        except FileNotFoundError:
            return Response({'error': 'File not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def filter_data(self, data, school_param, account_name_param):
        filtered_data = []

        for item in data:
            if (school_param is None or str(item.get('school')) == school_param) and \
               (account_name_param is None or item.get('login') == account_name_param):
                filtered_data.append(item)

        return filtered_data