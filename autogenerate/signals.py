from django.db.models.signals import post_save
from django.dispatch import receiver
from autogenerate.models import Schedule, WeekDay
from admin_app.models import Ring
from django.db.models import Q

@receiver(post_save, sender=Schedule)
def attach_rings_to_weekdays(sender, instance, created, **kwargs):
    if created:
        # Получаем все ринги для определенной школы
        rings_for_school = Ring.objects.filter(Q(school=instance.teacher.school) | Q(school=None))
        # Получаем или создаем объекты WeekDay для расписания
        week_days = WeekDay.objects.all()
        # Привязываем все полученные ринги к каждому дню недели
        for week_day in week_days:
            week_day.class_hours.add(*rings_for_school)
