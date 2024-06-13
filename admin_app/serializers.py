from rest_framework import serializers
from auth_user.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
# from .models import User
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'school', 'role']

# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','is_superuser', 'email', 'username', 'school']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class ProudOfSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProudOfSchool
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id','classroom_name', 'classroom_number', 'flat', 'korpus','school']
        read_only_fields = ['school']

class ClassSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), required=False, allow_null=True)
    class_teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), required=False, allow_null=True)

    class Meta:
        model = ClassGroup
        fields = ['id', 'class_name', 'class_number', 'language', 'classroom', 'class_teacher', 'osnova_plan', 'osnova_smena', 'dopurok_plan', 'dopurok_smena', 'school']
        read_only_fields = ['school']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Проверяем наличие classroom_id и преобразуем в соответствующий объект или None
        representation['classroom'] = (AvailableClassRoomSerializer(instance.classroom).data
                                        if instance.classroom_id is not None else None)

        # Проверяем наличие class_teacher_id и преобразуем в соответствующий объект или None
        representation['class_teacher'] = (AvailableTeacherSerializer(instance.class_teacher).data
                                            if instance.class_teacher_id is not None else None)

        return representation

class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['id','plan','smena','number','start_time','end_time','school']
        read_only_fields = ['school']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','food_name','food_sostav','vihod_1','vihod_2','vihod_3','week_day','school']
        read_only_fields = ['school']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id','slider_name','slider_photo','school']
        read_only_fields = ['school']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','full_name','type','school']
        read_only_fields = ['school']

class schoolPasportApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolPasport
        fields = ['id','school_address', 'photo','established', 'amount_of_children','ul_sany','kiz_sany','school_lang','status','vmestimost','dayarlyk_class_number','dayarlyk_student_number','number_of_students','number_of_classes','number_of_1_4_students','number_of_1_4_classes','number_of_5_9_students','number_of_5_9_classes','number_of_10_11_students','number_of_10_11_classes','amount_of_family','amount_of_parents','all_pedagog_number','pedagog_sheber','pedagog_zertteushy','pedagog_sarapshy','pedagog_moderator','pedagog','pedagog_stazher','pedagog_zhogary','pedagog_1sanat','pedagog_2sanat','pedagog_sanat_zhok','school_history','school']
        read_only_fields = ['school']

class School_AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Administration
        fields = ['id','administrator_name','administator_photo','position','school']
        read_only_fields = ['school']

# ======================================================================
class AvailableSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_kz_name', 'url']

class AvailableTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'school']

class AvailableRingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['id', 'start_time', 'end_time','plan','smena','number','school']

class AvailableDopUrokRingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopUrokRing
        fields = ['id', 'start_time', 'end_time','plan','smena','number']

class AvailableSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'full_name','type','school']

class AvailableClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'classroom_name','classroom_number', 'school']

class AvailableClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = ['id', 'class_name', 'class_number', 'class_letter', 'school']
        read_only_fields = ['school']



class Sport_SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Success
        fields = ['id','fullname','photo','student_success','school']
        read_only_fields = ['school']

class Oner_SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oner_Success
        fields = ['id','fullname','photo','student_success','school']
        read_only_fields = ['school']



class PandikOlimpiada_SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PandikOlimpiada_Success
        fields = ['id','fullname','photo','student_success','school']
        read_only_fields = ['school']

class RedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedCertificate
        fields = ['id','fullname','photo','student_success','school']
        read_only_fields = ['school']

class AltynBelgiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AltynBelgi
        fields = ['id','fullname','photo','student_success','school']
        read_only_fields = ['school']

class School_SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_SocialMedia
        fields = ['id','type','account_name','qr_code','school']
        read_only_fields = ['school']

class School_DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Director
        fields = ['id','director_name','director_photo','phone_number','email','school']
        read_only_fields = ['school']


class Extra_LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_Lessons
        fields = ['id','type_full_name','school']
        read_only_fields = ['school']


class DopUrokSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopUrok
        fields = ['id', 'week_day', 'ring', 'classl', 'teacher', 'subject', 'classroom', 'teacher2', 'classroom2',
                  'subject2', 'typez', 'school']
        read_only_fields = ['school']

    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    ring = serializers.PrimaryKeyRelatedField(
        queryset=DopUrokRing.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    classl = serializers.PrimaryKeyRelatedField(
        queryset=ClassGroup.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    teacher2 = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    subject2 = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    classroom2 = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    typez = serializers.PrimaryKeyRelatedField(
        queryset=Extra_Lessons.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    def create(self, validated_data):
        teacher = validated_data.pop('teacher', None)
        ring = validated_data.pop('ring', None)
        classl = validated_data.pop('classl', None)
        subject = validated_data.pop('subject', None)
        classroom = validated_data.pop('classroom', None)
        teacher2 = validated_data.pop('teacher2', None)
        subject2 = validated_data.pop('subject2', None)
        classroom2 = validated_data.pop('classroom2', None)
        typez = validated_data.pop('typez', None)

        schedule = DopUrok.objects.create(**validated_data)

        if teacher:
            schedule.teacher = teacher
        if ring:
            schedule.ring = ring
        if classl:
            schedule.classl = classl
        if subject:
            schedule.subject = subject
        if classroom:
            schedule.classroom = classroom
        if teacher2:
            schedule.teacher2 = teacher2
        if subject2:
            schedule.subject2 = subject2
        if classroom2:
            schedule.classroom2 = classroom2
        if typez:
            schedule.typez = typez

        schedule.save()

        return schedule

    def update(self, instance, validated_data):
        instance.week_day = validated_data.get('week_day', instance.week_day)

        fields_to_update = ['teacher', 'ring', 'classl', 'subject', 'classroom', 'teacher2', 'subject2', 'classroom2',
                            'typez']

        for field in fields_to_update:
            field_value = validated_data.get(field)
            # Если значение равно None, присваиваем его в instance
            if field_value is not None:
                setattr(instance, field, field_value)
            # Если значение равно None и это поле может быть пустым (null=True), присваиваем None
            elif field in self.fields and getattr(self.fields[field], 'allow_null', False):
                setattr(instance, field, None)

        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super(DopUrokSerializer, self).to_representation(instance)

        # Для teacher
        teacher_instance = instance.teacher
        if teacher_instance:
            representation['teacher'] = AvailableTeacherSerializer(teacher_instance).data
        else:
            representation['teacher'] = None

        # Для ring
        ring_instance = instance.ring
        if ring_instance:
            representation['ring'] = AvailableDopUrokRingSerializer(ring_instance).data
        else:
            representation['ring'] = None

        # Для classl
        class_instance = instance.classl
        if class_instance:
            representation['classl'] = AvailableClassesSerializer(class_instance).data
        else:
            representation['classl'] = None

        # Для subject
        subject_instance = instance.subject
        if class_instance:
            representation['subject'] = AvailableSubjectSerializer(subject_instance).data
        else:
            representation['subject'] = None

        # Для classroom
        classroom_instance = instance.classroom
        if classroom_instance:
            representation['classroom'] = AvailableClassRoomSerializer(classroom_instance).data
        else:
            representation['classroom'] = None

        # Для teacher2
        teacher2_instance = instance.teacher2
        if teacher2_instance:
            representation['teacher2'] = AvailableTeacherSerializer(teacher2_instance).data
        else:
            representation['teacher2'] = None

        # Для subject2
        subject2_instance = instance.subject2
        if class_instance:
            representation['subject2'] = AvailableSubjectSerializer(subject2_instance).data
        else:
            representation['subject2'] = None

        # Для classroom2
        classroom2_instance = instance.classroom2
        if classroom2_instance:
            representation['classroom2'] = AvailableClassRoomSerializer(classroom2_instance).data
        else:
            representation['classroom2'] = None

        # Для typez

        typez_instance = instance.typez
        if typez_instance:
            representation['typez'] = Extra_LessonSerializer(typez_instance).data
        else:
            representation['typez'] = None

        return representation


class DopUrokRingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopUrokRing
        fields = ['id','plan','smena','number','start_time','end_time','school']
        read_only_fields = ['school']
# ==================================================================================================


class YearField(serializers.Field):
    def to_representation(self, obj):
        return obj.year if obj else None

    def to_internal_value(self, data):
        try:
            return serializers.DateTimeField().to_internal_value(f"{data}-01-01T00:00:00Z")
        except serializers.ValidationError:
            raise serializers.ValidationError("Invalid year format")


class JobHistoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = ['start_date', 'end_date', 'job_characteristic']


class JobHistoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = ['start_date', 'end_date', 'job_characteristic']



class SpecialityHistoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityHistory
        fields = ['end_date', 'speciality_university', 'mamandygy', 'degree']


class SpecialityHistoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityHistory
        fields = ['end_date', 'speciality_university', 'mamandygy', 'degree']



class TeacherReadSerializer(serializers.ModelSerializer):
    job_history = JobHistoryReadSerializer(many=True, read_only=True, source='jobhistory_set')
    speciality_history = SpecialityHistoryReadSerializer(many=True, read_only=True, source='specialityhistory_set')

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'photo3x4', 'pedagog', 'job_history', 'speciality_history', 'school']
        read_only_fields = ['school']


class TeacherWriteSerializer(serializers.ModelSerializer):
    job_history = JobHistoryWriteSerializer(many=True, required=False)
    speciality_history = SpecialityHistoryWriteSerializer(many=True, required=False)

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'photo3x4', 'pedagog', 'school', 'job_history', 'speciality_history']
        read_only_fields = ['school']

    def create(self, validated_data):
        job_history_data = validated_data.pop('job_history', [])
        speciality_history_data = validated_data.pop('speciality_history', [])

        teacher = Teacher.objects.create(**validated_data)

        for job_data in job_history_data:
            JobHistory.objects.create(teacher=teacher, **job_data)

        for speciality_data in speciality_history_data:
            SpecialityHistory.objects.create(teacher=teacher, **speciality_data)

        return teacher

    def update(self, instance, validated_data):
        job_history_data = validated_data.pop('job_history', [])
        speciality_history_data = validated_data.pop('speciality_history', [])

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.photo3x4 = validated_data.get('photo3x4', instance.photo3x4)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.pedagog = validated_data.get('pedagog', instance.pedagog)

        instance.save()

        instance.jobhistory_set.all().delete()
        for job_data in job_history_data:
            JobHistory.objects.create(teacher=instance, **job_data)

        instance.specialityhistory_set.all().delete()
        for speciality_data in speciality_history_data:
            SpecialityHistory.objects.create(teacher=instance, **speciality_data)

        return instance

    def to_representation(self, instance):
        representation = super(TeacherWriteSerializer, self).to_representation(instance)
        for job_history_entry in representation.get('job_history', []):
            job_history_entry['start_date'] = job_history_entry['start_date'].year if job_history_entry['start_date'] else None
            job_history_entry['end_date'] = job_history_entry['end_date'].year if job_history_entry['end_date'] else None

        for speciality_history_entry in representation.get('speciality_history', []):
            speciality_history_entry['end_date'] = speciality_history_entry['end_date'].year if speciality_history_entry['end_date'] else None

        return representation

class TeacherWorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherWorkload
        fields = '__all__'

# Kruzhok
# --------------------------------------------------------------------------------------------

class LessonReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['week_day', 'classroom', 'start_end_time']


class LessonWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['week_day', 'classroom', 'start_end_time']

class KruzhokReadSerializer(serializers.ModelSerializer):
    teacher = AvailableTeacherSerializer(read_only=True)
    lessons = LessonReadSerializer(many=True, read_only=True)

    class Meta:
        model = Kruzhok
        fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons']
        read_only_fields = ['school']

    def to_representation(self, instance):
        representation = super(KruzhokReadSerializer, self).to_representation(instance)

        teacher_data = AvailableTeacherSerializer(instance.teacher).data
        teacher = TeacherReadSerializer(instance.teacher).data
        photo3x4 = teacher.get('photo3x4')
        if photo3x4:
            representation['teacher'] = {
                'id': teacher_data.get('id'),
                'full_name': teacher_data.get('full_name'),
                'photo3x4': 'https://bilimge.kz' + photo3x4
            }
        representation['lessons'] = LessonReadSerializer(instance.lessons.all(), many=True).data

        return representation

class KruzhokWriteSerializer(serializers.ModelSerializer):
    lessons = LessonWriteSerializer(many=True, write_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        source='teacher',
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False
    )
    photo = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Kruzhok
        fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons', 'teacher_id']
        read_only_fields = ['school']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        teacher_id = validated_data.pop('teacher_id', None)
        photo = validated_data.pop('photo', None)

        kruzhok = Kruzhok.objects.create(**validated_data)

        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                kruzhok.teacher = teacher
                kruzhok.save()
            except Teacher.DoesNotExist:
                pass

        if photo:
            kruzhok.photo = photo
            kruzhok.save()

        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=kruzhok, **lesson_data)

        return kruzhok

    def update(self, instance, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        teacher_id = validated_data.pop('teacher_id', None)

        instance.kruzhok_name = validated_data.get('kruzhok_name', instance.kruzhok_name)
        instance.purpose = validated_data.get('purpose', instance.purpose)

        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                instance.teacher = teacher
                instance.save()
            except Teacher.DoesNotExist:
                pass

        Lesson.objects.filter(kruzhok=instance).delete()

        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=instance, **lesson_data)

        if 'photo' in validated_data:
            instance.photo = validated_data['photo']

        instance.save()

        return instance

class PhotoforNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoforNews
        fields = ['image']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'date', 'text', 'type', 'img1','img2','img3','img4','img5','img6','img7','img8','img9','img10', 'qr_code', 'school']
        read_only_fields = ['school','qr_code']

    def update(self, instance, validated_data):
        # Обновляем текст и тип новости
        instance.date = validated_data.get('date', instance.date)
        instance.text = validated_data.get('text', instance.text)
        instance.type = validated_data.get('type', instance.type)

        # Обновляем изображения, если они были предоставлены в данных
        for img_field in ['img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'img9', 'img10']:
            if img_field in validated_data:
                img_data = validated_data.pop(img_field)
                # Если img_data равен None, значит, изображение было удалено
                if img_data is None:
                    setattr(instance, img_field, None)
                else:
                    setattr(instance, img_field, img_data)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.qr_code:
            representation['qr_code'] = self.get_absolute_url(instance.qr_code.url)
        else:
            del representation['qr_code']  # Если qr_code None, удаляем его из представления

        return representation

    def get_absolute_photo_urls(self, photos_queryset):
        request = self.context['request']
        return [request.build_absolute_uri(photo.image.url) if photo.image else None for photo in photos_queryset]

    def get_absolute_url(self, url):
        request = self.context['request']
        return request.build_absolute_uri(url)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'week_day', 'ring', 'classl', 'teacher', 'subject', 'classroom', 'teacher2', 'classroom2',
                  'subject2', 'typez', 'school']
        read_only_fields = ['school']

    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    ring = serializers.PrimaryKeyRelatedField(
        queryset=Ring.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    classl = serializers.PrimaryKeyRelatedField(
        queryset=ClassGroup.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(),
        write_only=True,
        required=False,
        allow_null=True  # Разрешаем null значения
    )
    teacher2 = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    subject2 = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    classroom2 = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    typez = serializers.PrimaryKeyRelatedField(
        queryset=Extra_Lessons.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    def create(self, validated_data):
        teacher = validated_data.pop('teacher', None)
        ring = validated_data.pop('ring', None)
        classl = validated_data.pop('classl', None)
        subject = validated_data.pop('subject', None)
        classroom = validated_data.pop('classroom', None)
        teacher2 = validated_data.pop('teacher2', None)
        subject2 = validated_data.pop('subject2', None)
        classroom2 = validated_data.pop('classroom2', None)
        typez = validated_data.pop('typez', None)

        schedule = Schedule.objects.create(**validated_data)

        if teacher:
            schedule.teacher = teacher
        if ring:
            schedule.ring = ring
        if classl:
            schedule.classl = classl
        if subject:
            schedule.subject = subject
        if classroom:
            schedule.classroom = classroom
        if teacher2:
            schedule.teacher2 = teacher2
        if subject2:
            schedule.subject2 = subject2
        if classroom2:
            schedule.classroom2 = classroom2
        if typez:
            schedule.typez = typez

        schedule.save()

        return schedule

    def update(self, instance, validated_data):
        instance.week_day = validated_data.get('week_day', instance.week_day)

        fields_to_update = ['teacher', 'ring', 'classl', 'subject', 'classroom', 'teacher2', 'subject2', 'classroom2',
                            'typez']

        for field in fields_to_update:
            field_value = validated_data.get(field)
            if field_value is not None:
                setattr(instance, field, field_value)
            # Если значение равно None и это поле может быть пустым (null=True), присваиваем None
            elif field in self.fields and getattr(self.fields[field], 'allow_null', False):
                setattr(instance, field, None)

        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super(ScheduleSerializer, self).to_representation(instance)

        # Для teacher
        teacher_instance = instance.teacher
        if teacher_instance:
            representation['teacher'] = AvailableTeacherSerializer(teacher_instance).data
        else:
            representation['teacher'] = None

        # Для ring
        ring_instance = instance.ring
        if ring_instance:
            representation['ring'] = AvailableRingSerializer(ring_instance).data
        else:
            representation['ring'] = None

        # Для classl
        class_instance = instance.classl
        if class_instance:
            representation['classl'] = AvailableClassesSerializer(class_instance).data
        else:
            representation['classl'] = None

        # Для subject
        subject_instance = instance.subject
        if class_instance:
            representation['subject'] = AvailableSubjectSerializer(subject_instance).data
        else:
            representation['subject'] = None

        # Для classroom
        classroom_instance = instance.classroom
        if classroom_instance:
            representation['classroom'] = AvailableClassRoomSerializer(classroom_instance).data
        else:
            representation['classroom'] = None

        # Для teacher2
        teacher2_instance = instance.teacher2
        if teacher2_instance:
            representation['teacher2'] = AvailableTeacherSerializer(teacher2_instance).data
        else:
            representation['teacher2'] = None

        # Для subject2
        subject2_instance = instance.subject2
        if class_instance:
            representation['subject2'] = AvailableSubjectSerializer(subject2_instance).data
        else:
            representation['subject2'] = None

        # Для classroom2
        classroom2_instance = instance.classroom2
        if classroom2_instance:
            representation['classroom2'] = AvailableClassRoomSerializer(classroom2_instance).data
        else:
            representation['classroom2'] = None

        # Для typez

        typez_instance = instance.typez
        if typez_instance:
            representation['typez'] = Extra_LessonSerializer(typez_instance).data
        else:
            representation['typez'] = None

        return representation
    
class NotificationsSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%Y-%m-%d, %H:%M")

    class Meta:
        model = Notifications
        fields = ['id', 'text', 'created_at', 'school']

class SchoolMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMap
        fields = '__all__'


class MainSchoolPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSchoolPhoto
        fields = '__all__'

    def update(self, instance, validated_data):
        for img_field in ['photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8', 'photo9',
                          'photo10']:
            if img_field in validated_data:
                img_data = validated_data.pop(img_field)
                # Если img_data равен None, значит, изображение было удалено
                if img_data is None:
                    setattr(instance, img_field, None)
                else:
                    setattr(instance, img_field, img_data)

        instance.save()
        return instance


class MapCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapCoordinates
        fields = '__all__'


