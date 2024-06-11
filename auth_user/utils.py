import random
import string
from django.core.mail import send_mail
import os
import requests
import urllib.parse
from django.core.mail import send_mail
# Ваши учетные данные из Twilio
import logging

def generate_random_code(length=4):
    """Генерация случайного кода указанной длины."""
    return ''.join(random.choices(string.digits, k=length))


logger = logging.getLogger(__name__)

def send_reset_code_email(email, code):
    """Отправка электронного письма с кодом сброса пароля."""
    subject = 'Code for reset password'
    message = f'Your code: {code}'
    from_email = 'akimzhankonarbayev@yandex.ru'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def send_verification_code_email(email, code):
    """Отправка электронного письма с кодом сброса пароля."""
    subject = 'Code for verification'
    message = f'Your code: {code}'
    from_email = 'akimzhankonarbayev@yandex.ru'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

