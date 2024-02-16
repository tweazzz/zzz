from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        print(f"Trying to authenticate with username/email: {username}")

        user = UserModel.objects.filter(email=username).first()

        if not user:
            user = UserModel.objects.filter(username=username).first()

        if user and user.check_password(password) and self.user_can_authenticate(user):
            print("Authentication successful")
            return user
        elif user:
            print("Authentication failed")
            print(f"Password from request: {username} {password}")
            print(f"User found: {user.username}")
        else:
            print("User not found")

    def user_can_authenticate(self, user):
        return user.is_active