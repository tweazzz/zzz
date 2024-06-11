from django.contrib import admin
from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    path('generate-schedule/', GenerateScheduleView.as_view(), name='generate-schedule'),
    path('get-schedule/', GeneratedScheduleListView.as_view(), name='get-schedule'),
]