from auth_user.models import User
from django.utils.translation import gettext_lazy as _
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers
from djoser.serializers import TokenSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from admin_app.models import School
from .models import PasswordResetToken

class CustomUserSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(required=False)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=False)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'fio', 'school', 'role')
        extra_kwargs = {
            'fio': {'read_only': True},
            'school': {'read_only': True},
            'role': {'read_only': True},
        }

    def update(self, instance, validated_data):
        instance.fio = validated_data.get('fio', instance.fio)
        instance.school = validated_data.get('school', instance.school)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        return instance
    
class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    role = serializers.CharField(write_only=True)
    fio = serializers.CharField(required=False)

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = DjoserUserCreateSerializer.Meta.fields + ('role', 'fio',)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        role = validated_data.get('role')
        return validated_data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.fio = validated_data.get('fio', '')
        user.role = validated_data.get('role', '')
        user.save()
        return user



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
                self.fail("invalid_credentials", detail=_("Invalid login or password"))

        if self.user and self.user.is_active:
            request_path = self.context.get("request").path
            if 'client' in request_path and self.user.role != 'client':
                raise serializers.ValidationError({"non_field_errors": _("Invalid role for this endpoint.")})
            elif 'admin' in request_path and self.user.role != 'admin':
                raise serializers.ValidationError({"non_field_errors": _("Invalid role for this endpoint.")})
            return attrs

        self.fail("invalid_credentials", detail=_("Invalid login or password"))

    def to_representation(self, instance):
        return TokenSerializer(instance).data
    

# class PasswordResetTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PasswordResetToken
#         fields = ['email','code', 'is_active']
    
class PasswordResetVerifySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4, required=True)
    phone_number = serializers.CharField(max_length=13, required=True)