from django.db import models
from admin_app import models as admin_models
from autogenerate.utils import BaseModel
# Create your models here.


class Schedule(BaseModel):
    subgroup = models.BooleanField(default=False)
    teacher = models.ForeignKey(admin_models.Teacher, on_delete=models.CASCADE,
                                related_name="schedules")
    total_load = models.PositiveIntegerField(default=1)
    school_class = models.ForeignKey(admin_models.Class, on_delete=models.CASCADE,
                                     related_name='schedules')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE,
                                related_name='schedules')
    lessons_per_week = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return f'{self.school_class} {self.subject}'


class Subject(BaseModel):
    title = models.CharField(max_length=300)
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'
    type_choices = [
        (EASY, 'EASY'),
        (MEDIUM, 'MEDIUM'),
        (HARD, 'HARD'),
    ]
    subject_type = models.CharField(max_length=20, choices=type_choices)
    school = models.ForeignKey(admin_models.School, on_delete=models.CASCADE,
                               related_name='subjects')

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f'{self.title}'

class ClassRoom(BaseModel):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    flat = models.PositiveIntegerField(default=1)
    housing = models.PositiveIntegerField(default=1)
    school = models.ForeignKey(admin_models.School, on_delete=models.CASCADE,
                               related_name='class_rooms')

    class Meta:
        verbose_name_plural = 'ClassRooms'


class ClassHour(BaseModel):
    start_time = models.TimeField()
    end_time = models.TimeField()
    smena1 = "1"
    smena2 = "2"
    shiftchoices = [
        (smena1, "1"),
        (smena2, "2"),
    ]
    shift = models.CharField(max_length=10, choices=shiftchoices)

    class Meta:
        verbose_name_plural = 'ClassHours'
    
    def __str__(self):
        return f'{self.start_time} {self.end_time}'


class WeekDay(BaseModel):
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    Saturday = "6"
    WEEK_DAY_CHOICES = [
        (Monday, "1"),
        (Tuesday, "2"),
        (Wednesday, "3"),
        (Thursday, "4"),
        (Friday, "5"),
        (Saturday, "6")
    ]
    value = models.CharField(max_length=20, choices=WEEK_DAY_CHOICES)
    class_hours = models.ManyToManyField(ClassHour, related_name='week_days')

    class Meta:
        verbose_name_plural = 'WeekDays'
    def __str__(self):
        return f'{self.value}'


class ClassSubject(BaseModel):
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE, related_name='class_subjects')
    class_hour = models.ForeignKey(ClassHour, on_delete=models.CASCADE,
                                   related_name='class_subjects')
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
                                   related_name='class_subjects')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='class_subjects')

    class Meta:
        verbose_name_plural = 'ClassSubjects'

    def __str__(self):
        return f'{self.schedule} {self.week_day} {self.class_hour}'
