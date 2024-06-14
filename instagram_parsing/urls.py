from django.contrib import admin
from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    path('schools/<int:school_id>/instagram-posts/', InstagramPostListView.as_view(), name='instagram-post-list-create'),

]