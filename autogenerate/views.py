from rest_framework.views import APIView
from rest_framework import permissions
from autogenerate import serializers, models, constants
from admin_app import models as admin_models
from rest_framework.response import Response
from rest_framework import status
import random
from django.db.models import Count
from django.db.models import Q




class AutoSchedulerView(APIView):
    """
    WARNING:
    This code is for basic architecture, do not use it in stage/production environments.
    It realizes example of logic, to autogenerate schedule and may have bugs :)
    """

    serializer_class = serializers.AutoScheduleSerializer
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        """
        TODO: Write the correct logic to distribute lessons by day so that they alternate every other day
              Write subgroup logic
              Write logic for windows between lessons(2 hours may be)
              Add a new field for languages, and write logic for many languages for one day
              Write SCRIPT or HAND MIGRATIONS to create a WeekDay AND ClassHour objects
              Add a denormalization to models, because it may have a lot of join. This may slow down code
              Learn select_related and prefetch_related methods to increase speed performance. But be careful with memory leaks :D.
              And ETC, look to technical specification for more information
        """

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        school_class_id = validated_data['school_class'].id
        school_class = admin_models.Class.objects.get(id=school_class_id)
        subject_id = validated_data['subject'].id
        subject = admin_models.Subject.objects.get(id=subject_id)
        teacher_id = validated_data['teacher'].id
        teacher = admin_models.Teacher.objects.get(id=teacher_id)
        double_lesson = validated_data.get('double_lesson', False)

        # Определение значения MAX_LESSONS_PER_DAY в зависимости от double_lesson
        MAX_LESSONS_PER_DAY = constants.MAX_LESSONS_PER_DAY_DOUBLE if double_lesson else constants.MAX_LESSONS_PER_DAY_SINGLE


        schedule_data = {
            'teacher': teacher,
            'school_class': school_class,
            'subject': subject,
            'subgroup': validated_data['subgroup'],
            'total_load': validated_data['total_load'],
            'lessons_per_week': validated_data['lessons_per_week'],
            'double_lesson': double_lesson,
            'school': request.user.school
        }

        schedule = models.Schedule.objects.create(**schedule_data)
        week_days = models.WeekDay.objects.all()
        

        if validated_data['subgroup']:
            try:
                existing_class_subjects = models.ClassSubject.objects.filter(
                    Q(schedule__school=request.user.school) &
                    Q(schedule__school_class=school_class) &
                    Q(schedule__subject=subject) &
                    Q(schedule__lessons_per_week=validated_data['lessons_per_week']) &
                    Q(schedule__double_lesson=validated_data['double_lesson']) &
                    Q(schedule__total_load=validated_data['total_load']) &
                    Q(schedule__subgroup=True)
                )

                # Если найдены существующие объекты для подгруппы, копируем их
                if existing_class_subjects.exists():
                    print("Copying existing subgroup schedules")
                    for existing_subject in existing_class_subjects:
                        models.ClassSubject.objects.create(
                            week_day=existing_subject.week_day,
                            class_hour=existing_subject.class_hour,
                            schedule=schedule,
                            school=request.user.school
                        )
                    # Пропускаем создание новых объектов
                    return Response({'message': 'Existing subgroup schedules copied'}, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                pass

        for week_day_idx, week_day in enumerate(week_days):
            print(f"Processing Week Day: {week_day}")
            class_hours = week_day.class_hours.filter(smena=school_class.osnova_smena)

            for class_hour_idx, class_hour in enumerate(class_hours):
                print(f"Processing Class Hour: {class_hour}")
                if not self._validate_subject(
                    class_hour_idx=class_hour_idx,
                    class_hours=class_hours,
                    subject=subject,
                ):
                    print("Skipping due to subject validation")
                    continue

                teacher_schedule = models.ClassSubject.objects.filter(
                    week_day=week_day,
                    class_hour=class_hour,
                    schedule__teacher=teacher
                )

                if teacher_schedule.exists():
                    print("Skipping due to teacher schedule conflict")
                    continue

                existing_class_subject = models.ClassSubject.objects.filter(
                    week_day=week_day,
                    class_hour=class_hour,
                    schedule__school_class=school_class
                ).exists()
                if existing_class_subject:
                    print("Skipping due to existing class subject")
                    continue

                teacher_class_subjects = models.ClassSubject.objects.filter(
                    schedule__teacher__school=teacher.school,
                    schedule__school_class=school_class.id,
                    schedule__subject=subject
                )

                if not self._validate_schedule(
                    schedule=schedule,
                    subject=subject,
                    teacher_class_subjects=teacher_class_subjects,
                    week_day=week_day,
                    MAX_LESSONS_PER_DAY=MAX_LESSONS_PER_DAY
                ):
                    print("Skipping due to schedule validation")
                    continue

                print("Creating Class Subject")
                models.ClassSubject.objects.create(
                    week_day=week_day,
                    class_hour=class_hour,
                    schedule=schedule,
                    school=self.request.user.school
                )

        return Response({'message': 'Schedule generated successfully'}, status=status.HTTP_201_CREATED)

    @staticmethod
    def _validate_subject(*args, **kwargs):
        is_last_hour = kwargs['class_hour_idx'] == len(kwargs['class_hours']) - 1
        is_hard_subject = kwargs['subject'].type == "HARD"

        if is_hard_subject and is_last_hour:
            return False

        return True


    @staticmethod
    def _validate_schedule(*args, **kwargs):
        teacher_class_subjects = kwargs['teacher_class_subjects']
        MAX_LESSONS_PER_DAY = kwargs['MAX_LESSONS_PER_DAY']

        if teacher_class_subjects.count() >= kwargs['schedule'].total_load:
            print("Exceeded total load")
            return False

        class_subject_week_days_count = len(set(
            teacher_class_subjects.values_list('week_day__id', flat=True)
        ))
        if class_subject_week_days_count > kwargs['schedule'].lessons_per_week:
            print("Exceeded lessons per week")
            return False

        # Считаем общее количество уроков на неделе
        total_lessons_this_week = teacher_class_subjects.count()

        if total_lessons_this_week >= kwargs['schedule'].total_load:
            print("Exceeded total load for this week")
            return False

        today_class_subjects = teacher_class_subjects.filter(
            week_day=kwargs['week_day']
        )

        if today_class_subjects.count() >= MAX_LESSONS_PER_DAY:
            print("Exceeded max lessons per day")
            return False

        return True

    

class GenerateSubjectView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # Получаем объекты ClassSubject, фильтруем их по школе пользователя
        user_school = request.user.school


        # Удаляем все Schedule, принадлежащие пользовательской школе
        admin_models.Schedule.objects.filter(school=user_school).delete()

        
        class_subjects = models.ClassSubject.objects.filter(school=user_school)

        # Создаем объекты Schedule в приложении admin_app, используя данные из ClassSubject
        for class_subject in class_subjects:
            admin_models.Schedule.objects.create(
                school=user_school,
                week_day=class_subject.week_day,
                subject=class_subject.schedule.subject,
                classl=class_subject.schedule.school_class,
                teacher=class_subject.schedule.teacher,
                ring=class_subject.class_hour
            )

        return Response({'message': 'ClassSubjects synchronized with Schedule successfully'}, status=status.HTTP_201_CREATED)