from django.contrib import admin
from .models import PasswordResetToken

# Register your models here.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'digisav',
        'USER': 'kestesikz',
        'PASSWORD': 'digisav',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}