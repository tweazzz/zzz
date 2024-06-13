from django_filters import rest_framework as filters
from admin_app.models import *
from django.db import models
import django_filters


# class AdminFilter(filters.FilterSet):
#     class Meta:
#         model = User
#         fields = '__all__'


class NewsFilter(filters.FilterSet):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['img1','img2','img3','img4','img5','img6','img7','img8','img9','img10','qr_code']

class SchoolFilter(filters.FilterSet):
    class Meta:
        model = School
        fields = '__all__'
        exclude = ['logo','school_map','qrcode']

class ClassFilter(filters.FilterSet):
    class Meta:
        model = ClassGroup
        fields = '__all__'

class ClassroomFilter(filters.FilterSet):
    class Meta:
        model = Classroom
        fields = '__all__'

class SubjectFilter(filters.FilterSet):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')
    school__id = django_filters.NumberFilter(field_name='school__id')
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['photo3x4']

class DopUrokFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')
    class Meta:
        model = DopUrok
        fields = '__all__'

class DopUrokRingFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')
    class Meta:
        model = DopUrokRing
        fields = '__all__'


class Extra_LessonsFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Extra_Lessons
        fields = '__all__'

class KruzhokFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Kruzhok
        fields = '__all__'
        exclude = ['photo']

class MenuFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Menu
        fields = '__all__'


class PandikOlimpiada_SuccessFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = PandikOlimpiada_Success
        fields = '__all__'
        exclude = ['photo']

class AltynBelgiFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = AltynBelgi
        fields = '__all__'
        exclude = ['photo']

class Oner_SuccessFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Oner_Success
        fields = '__all__'
        exclude = ['photo']

class Sport_SuccessFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Sport_Success
        fields = '__all__'
        exclude = ['photo']

class RedCertificateFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = RedCertificate
        fields = '__all__'
        exclude = ['photo']

class RingFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Ring
        fields = '__all__'

class ScheduleFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')
    subject = django_filters.CharFilter()
    class_group = django_filters.CharFilter()
    teacher = django_filters.CharFilter()
    classroom = django_filters.CharFilter()
    typez = django_filters.CharFilter()
    ring = django_filters.CharFilter()
    class Meta:
        model = Schedule
        # fields = ['school','subject','class_group','teacher','classroom','typez','ring']
        fields = '__all__'

class School_AdministrationFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = School_Administration
        fields = '__all__'
        exclude = ['administator_photo']

class School_DirectorFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = School_Director
        fields = '__all__'
        exclude = ['director_photo']

class School_PasportFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = schoolPasport
        fields = '__all__'
        exclude = ['photo']

class School_SocialMediaFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = School_SocialMedia
        fields = '__all__'
        exclude = ['qr_code']


class SliderFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Slider
        fields = '__all__'
        exclude = ['slider_photo']


class AvailableClassesFilter(filters.FilterSet):
    class Meta:
        model = ClassGroup
        fields = ['id','class_name','class_number']

class AvailableRingFilter(filters.FilterSet):
    class Meta:
        model = Ring
        fields = ['id','start_time','end_time']


class AvailableDopUrokRingFilter(filters.FilterSet):
    class Meta:
        model = DopUrokRing
        fields = ['id','start_time','end_time']


class SchoolMapFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = SchoolMap
        fields = '__all__'
        exclude = ['map','flat1','flat2','flat3','flat4','flat5']


class MainSliderFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = MainSchoolPhoto
        fields = '__all__'
        exclude = ['photo1','photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10']


class ProudOfScoolFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = ProudOfSchool
        fields = '__all__'
        exclude = ['photo']


class NotificationsFilter(filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__url')

    class Meta:
        model = Notifications
        fields = '__all__'