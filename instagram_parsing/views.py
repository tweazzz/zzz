from django.shortcuts import render
from .models import InstagramPost
from .serializers import InstagramPostSerializer
from rest_framework import generics
# Create your views here.


class InstagramPostListView(generics.ListAPIView):
    serializer_class = InstagramPostSerializer

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return InstagramPost.objects.filter(school_id=school_id).select_related('school')
