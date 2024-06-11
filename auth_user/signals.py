from django.db.models.signals import post_save
from django.dispatch import receiver
from admin_app.models import Notifications
from .models import User
from fcm_django.models import FCMDevice


@receiver(post_save, sender=Notifications)
def send_push_notification(sender, instance, created, **kwargs):
    if created:
        school_id = instance.school_id
        users = User.objects.filter(school_id=school_id).exclude(role='admin')

        devices = FCMDevice.objects.filter(user__in=users)

        # Отправляем уведомления
        try:
            devices.send_message(title="New Notification", message=instance.text)

            # Выводим информацию о пользователях, которым было отправлено уведомление
            for user in users:
                print(f"Уведомление отправлено пользователю {user.username}")

            print(f"Уведомление успешно отправлено для школы {instance.school_id}")
        except Exception as e:
            print(f"Ошибка при отправке уведомления для школы {instance.school_id}: {e}")
