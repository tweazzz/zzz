import random
import string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from .tokens import account_activation_token  # Предполагается, что у вас есть файл tokens.py с определением токена
from typing import Type
from .models import User


def generate_random_code(length=4):
    """Генерация случайного кода указанной длины."""
    return ''.join(random.choices(string.digits, k=length))

def send_reset_code_email(email, code):
    """Отправка электронного письма с кодом сброса пароля."""
    subject = 'Code for reset password'
    message = f'Your code: {code}'
    from_email = 'akimzhankonarbayev@yandex.ru'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def send_verification(instance: Type[User], request):
    subject = 'Добро пожаловать!'
    from_mail = settings.EMAIL_HOST_USER
    to_list = [instance.email, ]
    current_site = get_current_site(request)
    domain_name = current_site.domain
    if 'media.' in domain_name:
        domain_name = domain_name.replace('media.', '')
    protocol = 'https://' if request.is_secure() else 'http://'
    email_tmp = render_to_string(
        'client_email_verify.html',
        {
            'domain': protocol + domain_name,
            'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
            'token': account_activation_token.make_token(instance)
        }
    )
    as_send_email(subject, email_tmp, from_mail, to_list)


def as_send_email(subject, email_tmp, from_mail, to_list):
    msg = EmailMultiAlternatives(subject, email_tmp, from_mail, to_list)
    msg.attach_alternative(email_tmp, "text/html")
    msg.send()


def activate(request, uidb64, token):
    url = activate_user(request, uidb64, token)
    return redirect(url)


def activate_user(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    current_site = get_current_site(request)
    domain_name = current_site.domain.split(":")[0]
    if 'media.' in domain_name:
        domain_name = domain_name.replace('media.', '')
    protocol = "https://" if request.is_secure() else "http://"
    url = f"{protocol}{domain_name}/"
    try:
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
    return url