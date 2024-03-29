from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from admin_app.models import School
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, unique=True)
    password = models.CharField(_('password'), max_length=128)
    phone_number = models.CharField(max_length=12)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name='admin_user')
    date_joined = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.school and not self.school.user_id:
            self.school.user_id = self.id
            self.school.save()
            print(f"School's user_id set to {self.id}")

    def __str__(self):
        return f'{self.email}'

@receiver(pre_save, sender=User)
def check_school_uniqueness(sender, instance, **kwargs):
    if instance.role == 'admin':
        if User.objects.filter(school=instance.school, role='admin').exclude(id=instance.id).exists():
            raise ValidationError({"school": "This school already has an administrator."})



class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, max_length=12)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Reset Token for {self.user.username}'
    

    # EREPAH9KLNYWPXCDZZLPLT2W