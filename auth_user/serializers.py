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
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=False)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=False)
    password = serializers.CharField(write_only=True, required=False)
    school_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'school', 'school_url', 'role', 'password')
        extra_kwargs = {
            'school': {'read_only': True},
            'role': {'read_only': True},
            'username': {'required': False}
        }

    def validate(self, data):
        password = data.get('password')
        if not password and self.instance is None:
            raise serializers.ValidationError("Password is required")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save(update_fields=['password'])
        return instance

    def get_school_url(self, obj):
        if obj.school:
            return obj.school.url
        else:
            return None


class UserMeSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=False)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=False)
    school_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'school', 'school_name', 'role', 'is_superuser')
        extra_kwargs = {
            'school': {'read_only': True},
            'role': {'read_only': True},
        }

    def get_school_name(self, obj):
        return obj.school.school_kz_name if obj.school else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['school_name'] = self.get_school_name(instance)
        return representation


class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    role = serializers.CharField(write_only=True)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=False)

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = DjoserUserCreateSerializer.Meta.fields + ('role', 'school',)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        role = validated_data.get('role')
        return validated_data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.role = validated_data.get('role', '')
        user.school = validated_data.get('school', None)
        user.is_active = True if validated_data.get('role') == 'admin' else False
        user.save()
        return user


from djoser.serializers import TokenCreateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import serializers


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
            if 'client' in request_path and self.user.role != 'admin':
                return attrs
            elif 'admin' in request_path and (self.user.role != 'admin' and not self.user.is_superuser):
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
    email = serializers.EmailField()


from fcm_django.models import FCMDevice


class FCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = '__all__'