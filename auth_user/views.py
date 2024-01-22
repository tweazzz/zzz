from django.shortcuts import render
from .models import User,PasswordResetToken
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializers import CustomUserCreateSerializer, CustomTokenCreateSerializer
from djoser.views import UserViewSet, TokenCreateView
from .serializers import CustomUserSerializer 
from django.contrib.auth import get_user_model
from .utils import generate_random_code, send_reset_code_email
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password



User = get_user_model()
class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
    http_method_names = ['get','head','options','put','patch']

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

from django.utils import timezone

@api_view(['POST'])
def send_reset_code(request):
    if request.method == 'POST':
        email = request.data.get('email')

        try:
            # Поиск пользователя по email
            user = User.objects.get(email=email, role='client')
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Поиск существующего токена или создание нового
        reset_token, created = PasswordResetToken.objects.get_or_create(user=user)

        error_response = Response(
            {'error': 'The code has already been sent to your email'},
            status=status.HTTP_400_BAD_REQUEST
        )

        # Если токен уже активен, возвращаем ошибку
        if reset_token.is_active and timezone.now() - reset_token.created_at > timezone.timedelta(minutes=2):
            reset_token.is_active = False
            reset_token.save()
            return error_response
        elif reset_token.is_active:
            return error_response

        # Генерация нового кода
        new_code = generate_random_code()

        # Обновление записи в таблице PasswordResetToken
        reset_token.code = new_code
        reset_token.email = email
        reset_token.is_active = True
        reset_token.created_at = timezone.now()
        reset_token.save()

        # Отправка кода на почту пользователя
        send_reset_code_email(user.email, new_code)

        return Response({'message': 'The code has been successfully sent to your email'}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)




from .serializers import PasswordResetVerifySerializer
@api_view(['POST'])
def verify_reset_code(request):
    serializer = PasswordResetVerifySerializer(data=request.data)

    if serializer.is_valid():
        # Получаем код и email из сериализатора
        code = serializer.validated_data['code']
        email = serializer.validated_data['email']

        # Поиск токена сброса пароля
        reset_token = get_object_or_404(PasswordResetToken, code=code, user__email=email, is_active=True)

        # Возвращаем информацию для проверки кода и емейла
        return Response({'message': 'Код подтвержден', 'email': email}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reset_password(request):
    # Получаем email и код из запроса
    email = request.data.get('email')
    code = request.data.get('code')

    # Поиск токена сброса пароля
    reset_token = get_object_or_404(PasswordResetToken, code=code, email=email, is_active=True)

    # Получаем пользователя, связанного с токеном
    user = reset_token.user

    # Получаем новый пароль и его подтверждение из запроса
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    # Проверка на совпадение нового и подтвержденного паролей
    if new_password != confirm_password:
        return Response({'error': 'Пароли не совпадают'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Проверка на сложность пароля
        validate_password(new_password, user)
    except ValidationError as e:
        return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

    # Установка нового пароля для пользователя
    user.set_password(new_password)
    user.save()

    # Деактивация токена
    reset_token.is_active = False
    reset_token.save()

    return Response({'message': 'Пароль успешно сброшен'}, status=status.HTTP_200_OK)