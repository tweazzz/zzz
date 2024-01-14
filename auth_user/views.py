from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from djoser.serializers import UserCreateSerializer,TokenCreateSerializer
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserCreateSerializer, CustomTokenCreateSerializer
from djoser.views import UserViewSet, TokenCreateView



class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['role'] = 'admin'
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ClientUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['role'] = 'client'
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CustomTokenCreateView(TokenCreateView):
    serializer_class = CustomTokenCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._action(serializer)
        return Response(
            data=self.get_serializer(serializer.user.auth_token).data,
            status=status.HTTP_200_OK
        )



