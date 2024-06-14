from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from admin_app.models import *
from admin_app.serializers import *
from .permissions import IsClient
from admin_app.permissions import IsAdminSchool, IsSuperAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from admin_app.filters import *
from rest_framework import permissions, generics
from rest_framework import viewsets


class SchoolsApi(viewsets.ReadOnlyModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter


class ClassroomApi(viewsets.ReadOnlyModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Classroom.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Classroom.objects.all()
        return Classroom.objects.all()


class ClassApi(viewsets.ReadOnlyModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return ClassGroup.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else ClassGroup.objects.all()
        return ClassGroup.objects.all()


class ScheduleApi(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Schedule.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Schedule.objects.all()
        return Schedule.objects.all()


class MenuApi(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Menu.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Menu.objects.all()
        return Menu.objects.all()


class SliderApi(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SliderFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Slider.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Slider.objects.all()
        return Slider.objects.all()


class SubjectApi(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubjectFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Subject.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Subject.objects.all()
        return Subject.objects.all()


class schoolPasportApi(viewsets.ReadOnlyModelViewSet):
    model = schoolPasport
    photo_field = 'photo'
    queryset = schoolPasport.objects.all()
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_PasportFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return schoolPasport.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else schoolPasport.objects.all()
        return schoolPasport.objects.all()


class School_AdministrationApi(viewsets.ReadOnlyModelViewSet):
    queryset = School_Administration.objects.all()
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_AdministrationFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return School_Administration.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else School_Administration.objects.all()
        return School_Administration.objects.all()


class Sport_SuccessApi(viewsets.ReadOnlyModelViewSet):
    queryset = Sport_Success.objects.all()
    serializer_class = Sport_SuccessSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Sport_SuccessFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Sport_Success.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Sport_Success.objects.all()
        return Sport_Success.objects.all()


class Oner_SuccessApi(viewsets.ReadOnlyModelViewSet):
    queryset = Oner_Success.objects.all()
    serializer_class = Oner_SuccessSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oner_SuccessFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Oner_Success.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Oner_Success.objects.all()
        return Oner_Success.objects.all()


class PandikOlimpiadaApi(viewsets.ReadOnlyModelViewSet):
    queryset = PandikOlimpiada_Success.objects.all()
    serializer_class = PandikOlimpiada_SuccessSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PandikOlimpiada_SuccessFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return PandikOlimpiada_Success.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else PandikOlimpiada_Success.objects.all()
        return PandikOlimpiada_Success.objects.all()


class School_RedCertificateApi(viewsets.ReadOnlyModelViewSet):
    queryset = RedCertificate.objects.all()
    serializer_class = RedCertificateSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RedCertificateFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return RedCertificate.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else RedCertificate.objects.all()
        return RedCertificate.objects.all()


class School_AltynBelgiApi(viewsets.ReadOnlyModelViewSet):
    queryset = AltynBelgi.objects.all()
    serializer_class = AltynBelgiSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AltynBelgiFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return AltynBelgi.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else AltynBelgi.objects.all()
        return AltynBelgi.objects.all()


class School_SocialMediaApi(viewsets.ReadOnlyModelViewSet):
    queryset = School_SocialMedia.objects.all()
    serializer_class = School_SocialMediaSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_SocialMediaFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return School_SocialMedia.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else School_SocialMedia.objects.all()
        return School_SocialMedia.objects.all()


class School_DirectorApi(viewsets.ReadOnlyModelViewSet):
    queryset = School_Director.objects.all()
    serializer_class = School_DirectorSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_DirectorFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return School_Director.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else School_Director.objects.all()
        return School_Director.objects.all()


class Extra_LessonsApi(viewsets.ReadOnlyModelViewSet):
    queryset = Extra_Lessons.objects.all()
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Extra_LessonsFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Extra_Lessons.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Extra_Lessons.objects.all()
        return Extra_Lessons.objects.all()


class RingApi(viewsets.ReadOnlyModelViewSet):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RingFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Ring.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Ring.objects.all()
        return Ring.objects.all()


class TeacherApi(viewsets.ReadOnlyModelViewSet):
    model = Teacher
    photo_field = 'photo3x4'
    queryset = Teacher.objects.all()
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter
    serializer_class = TeacherReadSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        if self.request.user.is_authenticated:
            if self.request.user.role != 'admin':
                queryset = queryset.filter(school=self.request.user.school)
            elif self.request.user.is_superuser:
                queryset = queryset.select_related('school')
        return queryset.prefetch_related('jobhistory_set', 'specialityhistory_set')


class TeacherWorkloadApi(viewsets.ReadOnlyModelViewSet):
    queryset = TeacherWorkload.objects.all()
    serializer_class = TeacherWorkloadSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return TeacherWorkload.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else TeacherWorkload.objects.all()
        return TeacherWorkload.objects.all()


class KruzhokListApi(viewsets.ReadOnlyModelViewSet):
    model = Kruzhok
    photo_field = 'photo'
    queryset = Kruzhok.objects.all()
    serializer_class = KruzhokReadSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = KruzhokFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Kruzhok.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Kruzhok.objects.all()
        return Kruzhok.objects.all()


class DopUrokApi(viewsets.ReadOnlyModelViewSet):
    queryset = DopUrok.objects.all()
    serializer_class = DopUrokSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return DopUrok.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else DopUrok.objects.all()
        return DopUrok.objects.all()


class DopUrokRingApi(viewsets.ReadOnlyModelViewSet):
    queryset = DopUrokRing.objects.all()
    serializer_class = DopUrokRingSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokRingFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return DopUrokRing.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else DopUrokRing.objects.all()
        return DopUrokRing.objects.all()


class NewsApi(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsClient]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return News.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else News.objects.all()
        return News.objects.all()


class NotificationsApi(viewsets.ReadOnlyModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return Notifications.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else Notifications.objects.all()
        return Notifications.objects.all()


class SchoolMapApi(viewsets.ReadOnlyModelViewSet):
    queryset = SchoolMap.objects.all()
    serializer_class = SchoolMapSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role != 'admin':
            return SchoolMap.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else SchoolMap.objects.all()
        return SchoolMap.objects.all()
    # def get_queryset(self):
    #   if self.request.user.is_authenticated:
    #      return SchoolMap.objects.filter(school=self.request.user.school) if not self.request.user.is_superuser else SchoolMap.objects.all().select_related('school')
    # return SchoolMap.objects.all().select_related('school')


class ProudOfSchoolView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProudOfSchoolSerializer  # Добавляем атрибут serializer_class
    filter_backends = [DjangoFilterBackend]
    # filterset_class = ProudOfSchoolFilter
    queryset = ProudOfSchool.objects.all().select_related('school')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ProudOfSchool.objects.filter(
                school=self.request.user.school) if not self.request.user.is_superuser else ProudOfSchool.objects.all().select_related(
                'school')
        return ProudOfSchool.objects.all().select_related('school')
