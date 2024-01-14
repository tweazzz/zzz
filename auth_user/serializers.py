from rest_framework import serializers
from .models import User
from django.utils.translation import gettext_lazy as _
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers
from djoser.serializers import TokenSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from djoser.serializers import TokenCreateSerializer as DjoserTokenCreateSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'school', 'date_joined', 'is_active', 'is_staff')


class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    role = serializers.CharField(write_only=True)

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = DjoserUserCreateSerializer.Meta.fields + ('role',)  

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        role = validated_data.get('role')
        return validated_data



from djoser.serializers import TokenCreateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('auth_token',)

class CustomTokenCreateSerializer(TokenCreateSerializer):
    def create(self, validated_data):
        user = validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return token

    def validate(self, attrs):
        password = attrs.get("password")
        username = attrs.get("username")
        params = {"username": username}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user and self.user.is_active:
            # Кастомная проверка роли пользователя в зависимости от пути запроса
            request_path = self.context.get("request").path
            if 'client' in request_path and self.user.role != 'client':
                raise serializers.ValidationError({"non_field_errors": _("Invalid role for this endpoint.")})
            elif 'admin' in request_path and self.user.role != 'admin':
                raise serializers.ValidationError({"non_field_errors": _("Invalid role for this endpoint.")})
            return attrs
        self.fail("invalid_credentials")

    def to_representation(self, instance):
        return TokenSerializer(instance).data