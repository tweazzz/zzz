from rest_framework.views import APIView
from rest_framework import permissions

from autogenerate import serializers, models, constants

from rest_framework.response import Response
from rest_framework import status
import random
from django.db.models import Count

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
        school_class = models.admin_models.Class.objects.get(id=school_class_id)
        subject_id = validated_data['subject'].id
        subject = models.Subject.objects.get(id=subject_id)
        teacher_id = validated_data['teacher'].id
        teacher = models.admin_models.Teacher.objects.get(id=teacher_id)

        schedule_data = {
            'teacher': teacher,
            'school_class': school_class,
            'subject': subject,
            'subgroup': validated_data['subgroup'],
            'total_load': validated_data['total_load'],
            'lessons_per_week': validated_data['lessons_per_week'],
        }

        schedule = models.Schedule.objects.create(**schedule_data)
        week_days = models.WeekDay.objects.all()

        for week_day_idx, week_day in enumerate(week_days):
            class_hours = week_day.class_hours.filter(shift=school_class.osnova_smena)

            for class_hour_idx, class_hour in enumerate(class_hours):
                if not self._validate_subject(
                    class_hour_idx=class_hour_idx,
                    class_hours=class_hours,
                    subject=subject,
                ):
                    continue
                

                teacher_schedule = models.ClassSubject.objects.filter(
                    week_day=week_day,
                    class_hour=class_hour,
                    schedule__teacher=teacher
                )
                if teacher_schedule.exists():
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
                    week_day=week_day
                ):
                    continue

                engaged_class_rooms = models.ClassSubject.objects.filter(
                    week_day=week_day,
                    class_hour=class_hour,
                    schedule__teacher__school=teacher.school
                ).values_list('class_room__id', flat=True)

                class_room = models.ClassRoom.objects.exclude(
                    id__in=engaged_class_rooms
                ).first()

                if class_room:
                    models.ClassSubject.objects.create(
                        week_day=week_day,
                        class_hour=class_hour,
                        class_room=class_room,
                        schedule=schedule
                    )

        return Response({'message': 'Schedule generated successfully'}, status=status.HTTP_201_CREATED)


    @staticmethod
    def _validate_subject(*args, **kwargs):
        is_last_hour = kwargs['class_hour_idx'] == len(kwargs['class_hours']) - 1
        is_hard_subject = kwargs['subject'].subject_type == "HARD"

        if is_hard_subject and is_last_hour:
            return False

        return True

    @staticmethod
    def _validate_schedule(*args, **kwargs):
        teacher_class_subjects = kwargs['teacher_class_subjects']
        if teacher_class_subjects.count() >= kwargs['schedule'].total_load:
            return False

        class_subject_week_days_count = len(set(
            teacher_class_subjects.values_list('week_day__id', flat=True)
        ))
        if class_subject_week_days_count >= kwargs['schedule'].lessons_per_week:
            return False

        today_class_subjects = teacher_class_subjects.filter(
            week_day=kwargs['week_day']
        )
        if today_class_subjects.count() >= constants.MAX_LESSONS_PER_DAY:
            return False

        return True
    