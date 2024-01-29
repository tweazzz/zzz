import random
import string
from django.core.mail import send_mail
import os
from twilio.rest import Client

# Ваши учетные данные из Twilio
account_sid = "AC9e0bded21e7a727b1f4b9fc67e28bf40"
auth_token = "a83db74c4ea43fffccb639723c2cdc38"
verify_sid = "VAb52a1f5df7e3dde69946a4a571718293"
twilio_number = "+77475204678"

# Создаем клиента Twilio
client = Client(account_sid, auth_token)

def generate_random_code(length=4):
    """Генерация случайного кода указанной длины."""
    return ''.join(random.choices(string.digits, k=length))

def send_reset_code_sms(phone_number, code):
    """Отправка SMS с кодом сброса пароля."""
    try:
        message = client.messages.create(
            body=f'Your code: {code}',
            from_=twilio_number,
            to=phone_number
        )
        print(f'SMS отправлено с SID: {message.sid}')
        return True
    except Exception as e:
        print(f'Ошибка отправки SMS: {str(e)}')
        return False

