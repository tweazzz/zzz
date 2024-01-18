# from rest_framework import serializers
# from auth_user.models import User
# from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer, UserSerializer
# from admin_app.models import *
# from djoser.serializers import UserCreateSerializer, UserSerializer
# from django.contrib.auth import get_user_model

# class ClientUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'username', 'password', 'school', 'role']

# class SchoolSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = School
#         fields = '__all__'

# class ClassroomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classrooms
#         fields = ['id','classroom_name', 'classroom_number', 'flat', 'korpus','school']
#         read_only_fields = ['school']


# class ClassSerializer(serializers.ModelSerializer):
#     classroom = serializers.PrimaryKeyRelatedField(queryset=Classrooms.objects.all())
#     class_teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())

#     class Meta:
#         model = Class
#         fields = ['id', 'class_name', 'class_number', 'language', 'classroom', 'class_teacher', 'osnova_plan', 'osnova_smena', 'dopurok_plan', 'dopurok_smena', 'school']
#         read_only_fields = ['school']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['classroom'] = AvailableClassRoomSerializer(instance.classroom).data
#         representation['class_teacher'] = AvailableTeacherSerializer(instance.class_teacher).data
#         return representation


# class RingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ring
#         fields = ['id','plan','smena','number','start_time','end_time','school']
#         read_only_fields = ['school']

# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = ['id','food_name','food_reti','food_sostav','vihod_1','vihod_2','vihod_3','week_day','school']
#         read_only_fields = ['school']

# class SliderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Slider
#         fields = ['id','slider_name','slider_photo','school']
#         read_only_fields = ['school']

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = ['id','full_name','type','school']
#         read_only_fields = ['school']

# class schoolPasportApiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = schoolPasport
#         fields = ['id','school_address', 'photo','established', 'amount_of_children','ul_sany','kiz_sany','school_lang','status','vmestimost','dayarlyk_class_number','dayarlyk_student_number','number_of_students','number_of_classes','number_of_1_4_students','number_of_1_4_classes','number_of_5_9_students','number_of_5_9_classes','number_of_10_11_students','number_of_10_11_classes','amount_of_family','amount_of_parents','all_pedagog_number','pedagog_sheber','pedagog_zertteushy','pedagog_sarapshy','pedagog_moderator','pedagog','pedagog_stazher','pedagog_zhogary','pedagog_1sanat','pedagog_2sanat','pedagog_sanat_zhok','school_history','school']
#         read_only_fields = ['school']

# class School_AdministrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = School_Administration
#         fields = ['id','administrator_name','phone_number','administator_photo','position','school']
#         read_only_fields = ['school']

# # ======================================================================
# class AvailableSchoolSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = School
#         fields = ['id', 'school_kz_name']

# class AvailableTeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = ['id', 'full_name']

# class AvailableRingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ring
#         fields = ['id', 'start_time', 'end_time','plan','smena','number']

# class AvailableSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = ['id', 'full_name','type']

# class AvailableClassRoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classrooms
#         fields = ['id', 'classroom_name','classroom_number']

# class AvailableClassesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Class
#         fields = ['id', 'class_name', 'class_number']

# class Sport_SuccessSerializer(serializers.ModelSerializer):
#     class_id = serializers.PrimaryKeyRelatedField(
#         source='classl',
#         queryset=Class.objects.all(),
#         write_only=True,
#         required=False
#     )

#     class Meta:
#         model = Sport_Success
#         fields = ['id', 'fullname', 'photo', 'student_success', 'classl', 'school', 'class_id']
#         read_only_fields = ['school']

#     classl = serializers.SerializerMethodField()

#     def get_classl(self, obj):
#         return str(obj.classl) if obj.classl else None


# class Oner_SuccessSerializer(serializers.ModelSerializer):
#     class_id = serializers.PrimaryKeyRelatedField(
#         source='classl',
#         queryset=Class.objects.all(),
#         write_only=True,
#         required=False
#     )

#     class Meta:
#         model = Oner_Success
#         fields = ['id', 'fullname', 'photo', 'student_success', 'classl', 'school', 'class_id']
#         read_only_fields = ['school']

#     classl = serializers.SerializerMethodField()

#     def get_classl(self, obj):
#         return str(obj.classl) if obj.classl else None


# class PandikOlimpiada_SuccessSerializer(serializers.ModelSerializer):
#     class_id = serializers.PrimaryKeyRelatedField(
#         source='classl',
#         queryset=Class.objects.all(),
#         write_only=True,
#         required=False
#     )

#     class Meta:
#         model = PandikOlimpiada_Success
#         fields = ['id', 'fullname', 'photo', 'student_success', 'classl', 'school', 'class_id']
#         read_only_fields = ['school']

#     classl = serializers.SerializerMethodField()

#     def get_classl(self, obj):
#         return str(obj.classl) if obj.classl else None

# class RedCertificateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RedCertificate
#         fields = ['id','fullname','photo','student_success','endyear','school']
#         read_only_fields = ['school']

# class AltynBelgiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AltynBelgi
#         fields = ['id','fullname','photo','student_success','endyear','school']
#         read_only_fields = ['school']

# class School_SocialMediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = School_SocialMedia
#         fields = ['id','type','account_name','school']
#         read_only_fields = ['school']

# class School_DirectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = School_Director
#         fields = ['id','director_name','director_photo','phone_number','email','school']
#         read_only_fields = ['school']

# class Extra_LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Extra_Lessons
#         fields = ['id','type_full_name','type_color','school']
#         read_only_fields = ['school']


# class DopUrokSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DopUrok
#         fields = ['id', 'week_day', 'ring','ring_id', 'classl','classl_id', 'teacher', 'teacher_id', 'subject','subject_id', 'classroom','classroom_id', 'teacher2','teacher2_id', 'classroom2','classroom2_id', 'subject2','subject2_id', 'typez','typez_id', 'school']
#         read_only_fields = ['school']

#     teacher = serializers.PrimaryKeyRelatedField(
#         queryset=Teacher.objects.all(),
#         write_only=True,
#         required=False
#     )
#     ring = serializers.PrimaryKeyRelatedField(
#         queryset=Ring.objects.all(),
#         write_only=True,
#         required=False
#     )
#     classl = serializers.PrimaryKeyRelatedField(
#         queryset=Class.objects.all(),
#         write_only=True,
#         required=False
#     )
#     subject = serializers.PrimaryKeyRelatedField(
#         queryset=Subject.objects.all(),
#         write_only=True,
#         required=False
#     )
#     classroom = serializers.PrimaryKeyRelatedField(
#         queryset=Classrooms.objects.all(),
#         write_only=True,
#         required=False
#     )
#     teacher2 = serializers.PrimaryKeyRelatedField(
#         queryset=Teacher.objects.all(),
#         write_only=True,
#         required=False
#     )
#     subject2 = serializers.PrimaryKeyRelatedField(
#         queryset=Subject.objects.all(),
#         write_only=True,
#         required=False
#     )
#     classroom2 = serializers.PrimaryKeyRelatedField(
#         queryset=Classrooms.objects.all(),
#         write_only=True,
#         required=False
#     )
#     typez = serializers.PrimaryKeyRelatedField(
#         queryset=Extra_Lessons.objects.all(),
#         write_only=True,
#         required=False
#     )


#     def to_representation(self, instance):
#         representation = super(DopUrokSerializer, self).to_representation(instance)

#         teacher_id = representation.get('teacher_id')
#         if teacher_id:
#             try:
#                 teacher_instance = Teacher.objects.get(id=teacher_id)
#                 representation['teacher'] = AvailableTeacherSerializer(teacher_instance).data
#             except Teacher.DoesNotExist:
#                 pass

#         ring_id = representation.get('ring_id')
#         if ring_id:
#             try:
#                 ring_instance = Ring.objects.get(id=ring_id)
#                 representation['ring'] = AvailableRingSerializer(ring_instance).data
#             except Ring.DoesNotExist:
#                 pass

#         classl_id = representation.get('classl_id')
#         if classl_id:
#             try:
#                 class_instance = Class.objects.get(id=classl_id)
#                 representation['classl'] = AvailableClassesSerializer(class_instance).data
#             except Class.DoesNotExist:
#                 pass

#         subject_id = representation.get('subject_id')
#         if subject_id:
#             try:
#                 subject_instance = Subject.objects.get(id=subject_id)
#                 representation['subject'] = AvailableSubjectSerializer(subject_instance).data
#             except Subject.DoesNotExist:
#                 pass

#         classroom_id = representation.get('classroom_id')
#         if classroom_id:
#             try:
#                 classroom_instance = Classrooms.objects.get(id=classroom_id)
#                 representation['classroom'] = AvailableClassRoomSerializer(classroom_instance).data
#             except Classrooms.DoesNotExist:
#                 pass

#         teacher2_id = representation.get('teacher2_id')
#         if teacher2_id:
#             try:
#                 teacher2_instance = Teacher.objects.get(id=teacher2_id)
#                 representation['teacher2'] = AvailableTeacherSerializer(teacher2_instance).data
#             except Teacher.DoesNotExist:
#                 pass

#         subject2_id = representation.get('subject2_id')
#         if subject2_id:
#             try:
#                 subject2_instance = Subject.objects.get(id=subject2_id)
#                 representation['subject2'] = AvailableSubjectSerializer(subject2_instance).data
#             except Subject.DoesNotExist:
#                 pass

#         classroom2_id = representation.get('classroom2_id')
#         if classroom2_id:
#             try:
#                 classroom2_instance = Classrooms.objects.get(id=classroom2_id)
#                 representation['classroom2'] = AvailableClassRoomSerializer(classroom2_instance).data
#             except Classrooms.DoesNotExist:
#                 pass

#         typez_id = representation.get('typez_id')
#         if typez_id:
#             try:
#                 typez_instance = Extra_Lessons.objects.get(id=typez_id)
#                 representation['typez'] = Extra_LessonSerializer(typez_instance).data
#             except Extra_Lessons.DoesNotExist:
#                 pass

#         del representation['teacher_id']
#         del representation['ring_id']
#         del representation['classl_id']
#         del representation['subject_id']
#         del representation['classroom_id']
#         del representation['teacher2_id']
#         del representation['subject2_id']
#         del representation['classroom2_id']
#         del representation['typez_id']

#         return representation


# class DopUrokRingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DopUrokRing
#         fields = ['id','plan','smena','number','start_time','end_time','school']
#         read_only_fields = ['school']
# # ==================================================================================================


# class YearField(serializers.Field):
#     def to_representation(self, obj):
#         return obj.year if obj else None

#     def to_internal_value(self, data):
#         try:
#             return serializers.DateTimeField().to_internal_value(f"{data}-01-01T00:00:00Z")
#         except serializers.ValidationError:
#             raise serializers.ValidationError("Invalid year format")


# class JobHistoryReadSerializer(serializers.ModelSerializer):
#     start_date = YearField()
#     end_date = YearField()

#     class Meta:
#         model = JobHistory
#         fields = ['start_date', 'end_date', 'job_characteristic']


# class JobHistoryWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JobHistory
#         fields = ['start_date', 'end_date', 'job_characteristic']


# class SpecialityHistoryReadSerializer(serializers.ModelSerializer):
#     end_date = YearField()

#     class Meta:
#         model = SpecialityHistory
#         fields = ['end_date', 'speciality_university', 'mamandygy', 'degree']


# class SpecialityHistoryWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpecialityHistory
#         fields = ['end_date', 'speciality_university', 'mamandygy', 'degree']



# class TeacherReadSerializer(serializers.ModelSerializer):
#     job_history = JobHistoryReadSerializer(many=True, read_only=True, source='jobhistory_set')
#     speciality_history = SpecialityHistoryReadSerializer(many=True, read_only=True, source='specialityhistory_set')

#     class Meta:
#         model = Teacher
#         fields = ['id', 'full_name', 'photo3x4', 'subject', 'pedagog', 'job_history', 'speciality_history', 'school']
#         read_only_fields = ['school']


# class TeacherWriteSerializer(serializers.ModelSerializer):
#     job_history = JobHistoryWriteSerializer(many=True, required=False)
#     speciality_history = SpecialityHistoryWriteSerializer(many=True, required=False)

#     class Meta:
#         model = Teacher
#         fields = ['id', 'full_name', 'photo3x4', 'subject', 'pedagog', 'school', 'job_history', 'speciality_history']
#         read_only_fields = ['school']

#     def to_representation(self, instance):
#         representation = super(TeacherWriteSerializer, self).to_representation(instance)
#         for job_history_entry in representation.get('job_history', []):
#             job_history_entry['start_date'] = job_history_entry['start_date'].year if job_history_entry['start_date'] else None
#             job_history_entry['end_date'] = job_history_entry['end_date'].year if job_history_entry['end_date'] else None

#         for speciality_history_entry in representation.get('speciality_history', []):
#             speciality_history_entry['end_date'] = speciality_history_entry['end_date'].year if speciality_history_entry['end_date'] else None

#         return representation

# class TeacherWorkloadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TeacherWorkload
#         fields = '__all__'

# # Kruzhok
# # --------------------------------------------------------------------------------------------

# class LessonReadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ['week_day', 'start_end_time']

# class LessonWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ['week_day', 'start_end_time']

# class KruzhokReadSerializer(serializers.ModelSerializer):
#     teacher = AvailableTeacherSerializer(read_only=True)
#     lessons = LessonReadSerializer(many=True, read_only=True)

#     class Meta:
#         model = Kruzhok
#         fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons']
#         read_only_fields = ['school']

#     def to_representation(self, instance):
#         representation = super(KruzhokReadSerializer, self).to_representation(instance)

#         teacher_data = AvailableTeacherSerializer(instance.teacher).data
#         representation['teacher'] = {
#             'id': teacher_data.get('id'),
#             'full_name': teacher_data.get('full_name')
#         }

#         representation['lessons'] = LessonReadSerializer(instance.lessons.all(), many=True).data

#         return representation

# class KruzhokWriteSerializer(serializers.ModelSerializer):
#     lessons = LessonWriteSerializer(many=True, write_only=True)
#     teacher_id = serializers.PrimaryKeyRelatedField(
#         source='teacher',
#         queryset=Teacher.objects.all(),
#         write_only=True,
#         required=False
#     )
#     photo = serializers.ImageField(allow_null=True, required=False)

#     class Meta:
#         model = Kruzhok
#         fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons', 'teacher_id']
#         read_only_fields = ['school']

# class PhotoforNewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhotoforNews
#         fields = ['image']

# class NewsSerializer(serializers.ModelSerializer):
#     photos = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)

#     class Meta:
#         model = News
#         fields = ['id', 'date', 'text', 'type', 'photos', 'school']
#         read_only_fields = ['school']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['photos'] = self.get_absolute_photo_urls(instance.photos.all())
#         return representation

#     def get_absolute_photo_urls(self, photos_queryset):
#         request = self.context['request']
#         return [request.build_absolute_uri(photo.image.url) if photo.image else None for photo in photos_queryset]

# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = ['id', 'week_day', 'ring','ring_id', 'classl','classl_id', 'teacher', 'teacher_id', 'subject','subject_id', 'classroom','classroom_id', 'teacher2','teacher2_id', 'classroom2','classroom2_id', 'subject2','subject2_id', 'typez','typez_id', 'school']
#         read_only_fields = ['school']

#     teacher = serializers.PrimaryKeyRelatedField(
#         queryset=Teacher.objects.all(),
#         write_only=True,
#         required=False
#     )
#     ring = serializers.PrimaryKeyRelatedField(
#         queryset=Ring.objects.all(),
#         write_only=True,
#         required=False
#     )
#     classl = serializers.PrimaryKeyRelatedField(
#         queryset=Class.objects.all(),
#         write_only=True,
#         required=False
#     )
#     subject = serializers.PrimaryKeyRelatedField(
#         queryset=Subject.objects.all(),
#         write_only=True,
#         required=False
#     )
#     classroom = serializers.PrimaryKeyRelatedField(
#         queryset=Classrooms.objects.all(),
#         write_only=True,
#         required=False
#     )
#     teacher2 = serializers.PrimaryKeyRelatedField(
#         queryset=Teacher.objects.all(),
#         write_only=True,
#         required=False
#     )
#     subject2 = serializers.PrimaryKeyRelatedField(
#         queryset=Subject.objects.all(),
#         write_only=True,
#         required=False
#     )
#     classroom2 = serializers.PrimaryKeyRelatedField(
#         queryset=Classrooms.objects.all(),
#         write_only=True,
#         required=False
#     )
#     typez = serializers.PrimaryKeyRelatedField(
#         queryset=Extra_Lessons.objects.all(),
#         write_only=True,
#         required=False
#     )

#     def to_representation(self, instance):
#         representation = super(ScheduleSerializer, self).to_representation(instance)

#         teacher_id = representation.get('teacher_id')
#         if teacher_id:
#             try:
#                 teacher_instance = Teacher.objects.get(id=teacher_id)
#                 representation['teacher'] = AvailableTeacherSerializer(teacher_instance).data
#             except Teacher.DoesNotExist:
#                 pass

#         ring_id = representation.get('ring_id')
#         if ring_id:
#             try:
#                 ring_instance = Ring.objects.get(id=ring_id)
#                 representation['ring'] = AvailableRingSerializer(ring_instance).data
#             except Ring.DoesNotExist:
#                 pass

#         classl_id = representation.get('classl_id')
#         if classl_id:
#             try:
#                 class_instance = Class.objects.get(id=classl_id)
#                 representation['classl'] = AvailableClassesSerializer(class_instance).data
#             except Class.DoesNotExist:
#                 pass

#         subject_id = representation.get('subject_id')
#         if subject_id:
#             try:
#                 subject_instance = Subject.objects.get(id=subject_id)
#                 representation['subject'] = AvailableSubjectSerializer(subject_instance).data
#             except Subject.DoesNotExist:
#                 pass

#         classroom_id = representation.get('classroom_id')
#         if classroom_id:
#             try:
#                 classroom_instance = Classrooms.objects.get(id=classroom_id)
#                 representation['classroom'] = AvailableClassRoomSerializer(classroom_instance).data
#             except Classrooms.DoesNotExist:
#                 pass

#         teacher2_id = representation.get('teacher2_id')
#         if teacher2_id:
#             try:
#                 teacher2_instance = Teacher.objects.get(id=teacher2_id)
#                 representation['teacher2'] = AvailableTeacherSerializer(teacher2_instance).data
#             except Teacher.DoesNotExist:
#                 pass

#         subject2_id = representation.get('subject2_id')
#         if subject2_id:
#             try:
#                 subject2_instance = Subject.objects.get(id=subject2_id)
#                 representation['subject2'] = AvailableSubjectSerializer(subject2_instance).data
#             except Subject.DoesNotExist:
#                 pass

#         classroom2_id = representation.get('classroom2_id')
#         if classroom2_id:
#             try:
#                 classroom2_instance = Classrooms.objects.get(id=classroom2_id)
#                 representation['classroom2'] = AvailableClassRoomSerializer(classroom2_instance).data
#             except Classrooms.DoesNotExist:
#                 pass

#         typez_id = representation.get('typez_id')
#         if typez_id:
#             try:
#                 typez_instance = Extra_Lessons.objects.get(id=typez_id)
#                 representation['typez'] = Extra_LessonSerializer(typez_instance).data
#             except Extra_Lessons.DoesNotExist:
#                 pass

#         del representation['teacher_id']
#         del representation['ring_id']
#         del representation['classl_id']
#         del representation['subject_id']
#         del representation['classroom_id']
#         del representation['teacher2_id']
#         del representation['subject2_id']
#         del representation['classroom2_id']
#         del representation['typez_id']

#         return representation
    
# class NotificationsSerializer(serializers.ModelSerializer):
#     created_at = serializers.DateTimeField(format="%Y-%m-%d, %H:%M")

#     class Meta:
#         model = Notifications
#         fields = ['id', 'text', 'created_at', 'school']

# class SchoolMapSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SchoolMap
#         fields = '__all__'