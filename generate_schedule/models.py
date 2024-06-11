from django.db import models
from admin_app.models import *

# Create your models here.
class GeneratedSchedule(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    WEEK_DAY_CHOICES = [
        (Monday, "Monday"),
        (Tuesday, "Tuesday"),
        (Wednesday, "Wednesday"),
        (Thursday, "Thursday"),
        (Friday, "Friday"),
        (Saturday, "Saturday")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    ring = models.ForeignKey(Ring, on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
    shift = models.IntegerField()
    teacher2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True, related_name='teacher_g22')
    classroom2 = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True, related_name='classroom_g22')
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='subject_g22')
    typez = models.ForeignKey(Extra_Lessons, on_delete=models.CASCADE, null=True, blank=True)

    def start_time(self):
        return self.ring.start_time if self.ring else None

    def end_time(self):
        return self.ring.end_time if self.ring else None

    def __str__(self):
        return f'{self.school} {self.class_group} - {self.week_day}'