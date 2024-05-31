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
    subject = models.ForeignKey(admin_models.Subject, on_delete=models.CASCADE,
                                related_name='schedules')
    lessons_per_week = models.PositiveIntegerField(default=1)
    double_lesson = models.BooleanField(default=False)
    school = models.ForeignKey(admin_models.School, on_delete=models.SET_NULL, null=True,related_name='schedule_school')


    class Meta:
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return f'{self.school_class} {self.subject} {self.teacher}'

class WeekDay(BaseModel):
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    WEEK_DAY_CHOICES = [
        (Monday, "1"),
        (Tuesday, "2"),
        (Wednesday, "3"),
        (Thursday, "4"),
        (Friday, "5"),
    ]
    value = models.CharField(max_length=20, choices=WEEK_DAY_CHOICES)
    class_hours = models.ManyToManyField(admin_models.Ring, related_name='week_days',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'WeekDays'
    def __str__(self):
        return f'{self.value}'


class ClassSubject(BaseModel):
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE, related_name='class_subjects')
    class_hour = models.ForeignKey(admin_models.Ring, on_delete=models.CASCADE,
                                   related_name='class_subjects')
    # class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
    #                                related_name='class_subjects')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='class_subjects')
    school = models.ForeignKey(admin_models.School, on_delete=models.SET_NULL, null=True,related_name='classSubject_school')

    class Meta:
        verbose_name_plural = 'ClassSubjects'

    def __str__(self):
        return f'{self.schedule} {self.week_day} {self.class_hour} {self.schedule}'
