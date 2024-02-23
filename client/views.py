from django.shortcuts import render
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from admin_app.models import *
from admin_app.serializers import *
from .permissions import IsClient
from admin_app.permissions import IsAdminSchool,IsSuperAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from admin_app.filters import *
from rest_framework import permissions, generics



class SchoolsApi(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter

class ClassroomApi(generics.ListAPIView):
    queryset = Classrooms.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Classrooms.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Classrooms.objects.all()
        return Classrooms.objects.all()

class ClassApi(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Class.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Class.objects.all()
        return Class.objects.all()
    
class ScheduleApi(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Schedule.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Schedule.objects.all()
        return Schedule.objects.all()
    

class MenuApi(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuFilter


    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Menu.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Menu.objects.all()
        return Menu.objects.all()

class SliderApi(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SliderFilter


    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Slider.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Slider.objects.all()
        return Slider.objects.all()


class SubjectApi(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubjectFilter


    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Subject.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Subject.objects.all()
        return Subject.objects.all()


class schoolPasportApi(generics.ListAPIView):
    model = schoolPasport
    photo_field = 'photo'
    queryset = schoolPasport.objects.all()
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_PasportFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return schoolPasport.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else schoolPasport.objects.all()
        return schoolPasport.objects.all()


class School_AdministrationApi(generics.ListAPIView):
    queryset = School_Administration.objects.all()
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_AdministrationFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return School_Administration.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_Administration.objects.all()
        return School_Administration.objects.all()


class Sport_SuccessApi(generics.ListAPIView):
    queryset = Sport_Success.objects.all()
    serializer_class = Sport_SuccessSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Sport_SuccessFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Sport_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Sport_Success.objects.all()
        return Sport_Success.objects.all()


class Oner_SuccessApi(generics.ListAPIView):
    queryset = Oner_Success.objects.all()
    serializer_class = Oner_SuccessSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oner_SuccessFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Oner_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Oner_Success.objects.all()
        return Oner_Success.objects.all()
    


class PandikOlimpiadaApi(generics.ListAPIView):
    queryset = PandikOlimpiada_Success.objects.all()
    serializer_class = PandikOlimpiada_SuccessSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PandikOlimpiada_SuccessFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return PandikOlimpiada_Success.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else PandikOlimpiada_Success.objects.all()
        return PandikOlimpiada_Success.objects.all()


class School_RedCertificateApi(generics.ListAPIView):
    queryset = RedCertificate.objects.all()
    serializer_class = RedCertificateSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RedCertificateFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return RedCertificate.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else RedCertificate.objects.all()
        return RedCertificate.objects.all()


class School_AltynBelgiApi(generics.ListAPIView):
    queryset = AltynBelgi.objects.all()
    serializer_class = AltynBelgiSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AltynBelgiFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return AltynBelgi.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else AltynBelgi.objects.all()
        return AltynBelgi.objects.all()
    
class School_SocialMediaApi(generics.ListAPIView):
    queryset = School_SocialMedia.objects.all()
    serializer_class = School_SocialMediaSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_SocialMediaFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return School_SocialMedia.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_SocialMedia.objects.all()
        return School_SocialMedia.objects.all()

class School_DirectorApi(generics.ListAPIView):
    queryset = School_Director.objects.all()
    serializer_class = School_DirectorSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_DirectorFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return School_Director.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else School_Director.objects.all()
        return School_Director.objects.all()


class Extra_LessonsApi(generics.ListAPIView):
    queryset = Extra_Lessons.objects.all()
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Extra_LessonsFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Extra_Lessons.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Extra_Lessons.objects.all()
        return Extra_Lessons.objects.all()

class RingApi(generics.ListAPIView):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RingFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Ring.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Ring.objects.all()
        return Ring.objects.all()



class TeacherApi(generics.ListAPIView):
    model = Teacher
    photo_field = 'photo3x4'
    queryset = Teacher.objects.all()
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Teacher.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Teacher.objects.all()
        return Teacher.objects.all()

class TeacherWorkloadApi(generics.ListAPIView):
    queryset = TeacherWorkload.objects.all()
    serializer_class = TeacherWorkloadSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return TeacherWorkload.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else TeacherWorkload.objects.all()
        return TeacherWorkload.objects.all()




class KruzhokListApi(generics.ListAPIView):
    model = Kruzhok
    photo_field = 'photo'
    queryset = Kruzhok.objects.all()
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = KruzhokFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Kruzhok.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Kruzhok.objects.all()
        return Kruzhok.objects.all()

class DopUrokApi(generics.ListAPIView):
    queryset = DopUrok.objects.all()
    serializer_class = DopUrokSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return DopUrok.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else DopUrok.objects.all()
        return DopUrok.objects.all()


class DopUrokRingApi(generics.ListAPIView):
    queryset = DopUrokRing.objects.all()
    serializer_class = DopUrokRingSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokRingFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return DopUrokRing.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else DopUrokRing.objects.all()
        return DopUrokRing.objects.all()

class NewsApi(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return News.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else News.objects.all()
        return News.objects.all()
    
class NotificationsApi(generics.ListAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return Notifications.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else Notifications.objects.all()
        return Notifications.objects.all()
    
class SchoolMapApi(generics.ListAPIView):
    queryset = SchoolMap.objects.all()
    serializer_class = SchoolMapSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'client':
            return SchoolMap.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else SchoolMap.objects.all()
        return SchoolMap.objects.all()
    
