import random
import string
from django.core.mail import send_mail

def generate_random_code(length=4):
    """Генерация случайного кода указанной длины."""
    return ''.join(random.choices(string.digits, k=length))

def send_reset_code_email(email, code):
    """Отправка электронного письма с кодом сброса пароля."""
    subject = 'Code for reset password'
    message = f'Your code: {code}'
    from_email = 'your@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)