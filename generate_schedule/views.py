from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import School, ClassGroup, Subject, Teacher, Ring, TeacherSubject, Classroom
from .models import GeneratedSchedule
from .serializers import GenerateScheduleRequestSerializer, GeneratedScheduleSerializer
from rest_framework import generics
from collections import defaultdict
import logging




logger = logging.getLogger(__name__)

# class GenerateScheduleView(APIView):
#     serializer_class = GenerateScheduleRequestSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = GenerateScheduleRequestSerializer(data=request.data)
#         if serializer.is_valid():
#             school_id = serializer.validated_data['school_id']
#             try:
#                 school = School.objects.get(id=school_id)
#             except School.DoesNotExist:
#                 return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
#
#             class_groups = ClassGroup.objects.filter(school=school)
#             subjects = Subject.objects.filter(school=school).order_by('-priority')
#             rings = Ring.objects.filter(school=school)
#             week_days = [GeneratedSchedule.Monday, GeneratedSchedule.Tuesday, GeneratedSchedule.Wednesday,
#                          GeneratedSchedule.Thursday, GeneratedSchedule.Friday, GeneratedSchedule.Saturday]
#
#             def is_valid(schedule, new_entry):
#                 for entry in schedule:
#                     if entry['classroom'] == new_entry['classroom'] and entry['ring'] == new_entry['ring'] and entry[
#                         'week_day'] == new_entry['week_day']:
#                         logger.debug(
#                             f"Classroom conflict: {entry['classroom']} already has a class at {entry['ring']} on {entry['week_day']}")
#                         return False
#                     if entry['class_group'] == new_entry['class_group'] and entry['subject'] == new_entry['subject'] and \
#                             entry['week_day'] == new_entry['week_day']:
#                         logger.debug(
#                             f"Duplicate subject: {entry['class_group']} already has {entry['subject']} on {entry['week_day']}")
#                         return False
#                     if entry['shift'] != new_entry['shift']:
#                         logger.debug(f"Shift conflict: {entry['shift']} does not match {new_entry['shift']}")
#                         return False
#                 return True
#
#             def distribute_subjects(class_group_subject_hours):
#                 distributed = {}
#                 for class_group, subjects_hours in class_group_subject_hours.items():
#                     distributed[class_group] = {day: [] for day in week_days}
#                     for subject_id, hours in subjects_hours.items():
#                         days = week_days[:]
#                         while hours > 0 and days:
#                             day = days.pop(0)
#                             if len(distributed[class_group][day]) < len(rings):
#                                 distributed[class_group][day].append(subject_id)
#                                 hours -= 1
#                             else:
#                                 days.append(day)
#                 return distributed
#
#             def generate_schedule():
#                 schedule = []
#                 class_group_subject_hours = {
#                     class_group.id: {
#                         teacher_subject.subject.id: teacher_subject.hours_per_week
#                         for teacher_subject in TeacherSubject.objects.filter(class_group=class_group)
#                     }
#                     for class_group in class_groups
#                 }
#                 distributed_subjects = distribute_subjects(class_group_subject_hours)
#
#                 def backtrack(index):
#                     if index == len(class_groups) * len(week_days) * len(rings):
#                         return True
#
#                     class_group = class_groups[index // (len(week_days) * len(rings))]
#                     week_day = week_days[(index // len(rings)) % len(week_days)]
#                     ring = rings[index % len(rings)]
#                     subject_id = distributed_subjects[class_group.id][week_day].pop(0) if \
#                     distributed_subjects[class_group.id][week_day] else None
#
#                     if subject_id:
#                         subject = Subject.objects.get(id=subject_id)
#                         teacher_subjects = TeacherSubject.objects.filter(subject=subject, teacher__school=school,
#                                                                          class_group=class_group)
#                         for teacher_subject in teacher_subjects:
#                             teacher = teacher_subject.teacher
#                             if class_group.osnova_smena == ring.smena:
#                                 new_entry = {
#                                     'school': school,
#                                     'class_group': class_group,
#                                     'subject': subject,
#                                     'teacher': teacher,
#                                     'ring': ring,
#                                     'classroom': teacher_subject.classroom,
#                                     'week_day': week_day,
#                                     'shift': ring.smena,
#                                 }
#                                 if is_valid(schedule, new_entry):
#                                     schedule.append(new_entry)
#                                     logger.debug(
#                                         f"Scheduled {subject.full_name} for {class_group.class_name} with {teacher.full_name} at {ring.start_time} on {week_day}")
#                                     if backtrack(index + 1):
#                                         return True
#                                     schedule.pop()
#                                     distributed_subjects[class_group.id][week_day].insert(0, subject_id)
#                     else:
#                         if backtrack(index + 1):
#                             return True
#                     return False
#
#                 if not backtrack(0):
#                     return None
#                 return schedule
#
#             generated_schedule = generate_schedule()
#
#             if generated_schedule is None:
#                 return Response({'error': 'Failed to generate schedule.'},
#                                 status=status.HTTP_400_BAD_REQUEST)
#
#             for entry in generated_schedule:
#                 GeneratedSchedule.objects.create(
#                     school=entry['school'],
#                     class_group=entry['class_group'],
#                     subject=entry['subject'],
#                     teacher=entry['teacher'],
#                     ring=entry['ring'],
#                     classroom=entry['classroom'],
#                     week_day=entry['week_day'],
#                     shift=entry['shift'],
#                 )
#
#             return Response({'message': 'Schedule generated successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GenerateScheduleView(APIView):
#     serializer_class = GenerateScheduleRequestSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = GenerateScheduleRequestSerializer(data=request.data)
#         if serializer.is_valid():
#             school_id = serializer.validated_data['school_id']
#             try:
#                 school = School.objects.get(id=school_id)
#             except School.DoesNotExist:
#                 return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
#
#             class_groups = ClassGroup.objects.filter(school=school)
#             subjects = Subject.objects.filter(school=school).order_by('-priority')
#             rings = Ring.objects.filter(school=school)
#             week_days = [GeneratedSchedule.Monday, GeneratedSchedule.Tuesday, GeneratedSchedule.Wednesday, GeneratedSchedule.Thursday, GeneratedSchedule.Friday, GeneratedSchedule.Saturday]
#
#             def is_valid(schedule, new_entry):
#                 for entry in schedule:
#                     if entry['classroom'] == new_entry['classroom'] and entry['ring'] == new_entry['ring'] and entry['week_day'] == new_entry['week_day']:
#                         return False
#                     if entry['class_group'] == new_entry['class_group'] and entry['subject'] == new_entry['subject'] and entry['week_day'] == new_entry['week_day']:
#                         return False
#                     if entry['shift'] != new_entry['shift']:
#                         return False
#                 return True
#
#             def generate_schedule():
#                 schedule = []
#                 total_slots = len(class_groups) * len(week_days) * len(rings)
#
#                 def backtrack(index):
#                     if index == total_slots:
#                         return True
#
#                     class_group = class_groups[index // (len(week_days) * len(rings))]
#                     week_day = week_days[(index // len(rings)) % len(week_days)]
#                     ring = rings[index % len(rings)]
#
#                     for subject in subjects:
#                         teacher_subjects = TeacherSubject.objects.filter(subject=subject, teacher__school=school)
#                         for teacher_subject in teacher_subjects:
#                             teacher = teacher_subject.teacher
#                             if class_group.osnova_smena == ring.smena:
#                                 new_entry = {
#                                     'school': school,
#                                     'class_group': class_group,
#                                     'subject': subject,
#                                     'teacher': teacher,
#                                     'ring': ring,
#                                     'classroom': teacher_subject.classroom,
#                                     'week_day': week_day,
#                                     'shift': ring.smena,
#                                 }
#                                 if is_valid(schedule, new_entry):
#                                     schedule.append(new_entry)
#                                     if backtrack(index + 1):
#                                         return True
#                                     schedule.pop()
#                     return False
#
#                 if not backtrack(0):
#                     return None
#                 return schedule
#
#             generated_schedule = generate_schedule()
#
#             if generated_schedule is None:
#                 return Response({'error': 'Failed to generate schedule'}, status=status.HTTP_400_BAD_REQUEST)
#
#             for entry in generated_schedule:
#                 GeneratedSchedule.objects.create(
#                     school=entry['school'],
#                     class_group=entry['class_group'],
#                     subject=entry['subject'],
#                     teacher=entry['teacher'],
#                     ring=entry['ring'],
#                     classroom=entry['classroom'],
#                     week_day=entry['week_day'],
#                     shift=entry['shift'],
#                 )
#
#             return Response({'message': 'Schedule generated successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneratedScheduleListView(generics.ListAPIView):
    queryset = GeneratedSchedule.objects.all()
    serializer_class = GeneratedScheduleSerializer


class GenerateScheduleView(APIView):
    def post(self, request, school_id):
        GeneratedSchedule.objects.filter(school_id=school_id).delete()

        teacher_subjects = list(TeacherSubject.objects.filter(
            classroom__school_id=school_id,
            subject__type=Subject.INVARIANT
        ).order_by('-subject__importance'))

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        schedule = []
        teacher_schedule = {teacher.id: {day: [] for day in days} for teacher in
                            Teacher.objects.filter(school_id=school_id)}
        classroom_schedule = {classroom.id: {day: [] for day in days} for classroom in
                              Classroom.objects.filter(school_id=school_id)}

        def is_valid(teacher_id, classroom_id, day, start_time):
            if any(s.start_time() == start_time for s in teacher_schedule[teacher_id][day]):
                return False

            if any(s.start_time() == start_time for s in classroom_schedule[classroom_id][day]):
                return False

            return True

        def find_free_classroom(school_id, day, start_time):
            for classroom in Classroom.objects.filter(school_id=school_id):
                if all(s.start_time() != start_time for s in classroom_schedule[classroom.id][day]):
                    return classroom
            return None

        def get_ring_times(school_id, smena):
            return Ring.objects.filter(school_id=school_id, smena=smena)

        def backtrack(index):
            if index == len(teacher_subjects):
                return True

            ts = teacher_subjects[index]
            smena = ts.class_group.smena if ts.class_group else 1
            ring_times = get_ring_times(ts.classroom.school_id, smena)

            for ring in ring_times:
                day = ring.day_of_week
                start_time = ring.start_time
                end_time = ring.end_time
                classroom = find_free_classroom(ts.classroom.school_id, day, start_time)
                if classroom and is_valid(ts.teacher.id, classroom.id, day, start_time):
                    new_schedule = GeneratedSchedule(
                        week_day=day,
                        day_of_week=day,
                        shift=smena,
                        teacher=ts.teacher,
                        subject=ts.subject,
                        classroom=classroom,
                        class_group=ts.class_group,
                        ring=ring,
                        school_id=ts.classroom.school_id
                    )
                    schedule.append(new_schedule)
                    teacher_schedule[ts.teacher.id][day].append(new_schedule)
                    classroom_schedule[classroom.id][day].append(new_schedule)

                    if ts.subject.double:
                        double_scheduled = False
                        for double_ring in ring_times:
                            if double_ring != ring and is_valid(ts.teacher.id, classroom.id, day,
                                                                double_ring.start_time):
                                double_schedule = GeneratedSchedule(
                                    week_day=day,
                                    day_of_week=day,
                                    shift=smena,
                                    teacher=ts.teacher,
                                    subject=ts.subject,
                                    classroom=classroom,
                                    class_group=ts.class_group,
                                    ring=double_ring,
                                    school_id=ts.classroom.school_id
                                )
                                schedule.append(double_schedule)
                                teacher_schedule[ts.teacher.id][day].append(double_schedule)
                                classroom_schedule[classroom.id][day].append(double_schedule)
                                double_scheduled = True
                                break

                        if not double_scheduled:
                            schedule.remove(new_schedule)
                            teacher_schedule[ts.teacher.id][day].remove(new_schedule)
                            classroom_schedule[classroom.id][day].remove(new_schedule)
                            continue

                    if ts.subject.is_subgroup:
                        for other_ts in teacher_subjects:
                            if other_ts.subject == ts.subject and other_ts != ts:
                                other_classroom = find_free_classroom(ts.classroom.school_id, day, start_time)
                                if other_classroom and is_valid(other_ts.teacher.id, other_classroom.id, day,
                                                                start_time):
                                    new_schedule_sub = GeneratedSchedule(
                                        week_day=day,
                                        day_of_week=day,
                                        shift=smena,
                                        teacher=other_ts.teacher,
                                        subject=other_ts.subject,
                                        classroom=other_classroom,
                                        class_group=other_ts.class_group,
                                        ring=ring,
                                        school_id=ts.classroom.school_id
                                    )
                                    schedule.append(new_schedule_sub)
                                    teacher_schedule[other_ts.teacher.id][day].append(new_schedule_sub)
                                    classroom_schedule[other_classroom.id][day].append(new_schedule_sub)

                                    if backtrack(index + 1):
                                        return True

                                    schedule.remove(new_schedule_sub)
                                    teacher_schedule[other_ts.teacher.id][day].remove(new_schedule_sub)
                                    classroom_schedule[other_classroom.id][day].remove(new_schedule_sub)

                    if backtrack(index + 1):
                        return True

                    schedule.remove(new_schedule)
                    teacher_schedule[ts.teacher.id][day].remove(new_schedule)
                    classroom_schedule[classroom.id][day].remove(new_schedule)

            return False

        if backtrack(0):
            GeneratedSchedule.objects.bulk_create(schedule)
            return Response({'status': 'Schedule generated successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'Failed to generate schedule'}, status=status.HTTP_400_BAD_REQUEST)