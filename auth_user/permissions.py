from rest_framework import permissions

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем, авторизован ли пользователь
        if request.user and request.user.is_authenticated:
            # Проверяем, является ли роль пользователя клиентом
            if request.user.role != 'admin':
                # Разрешаем доступ для безопасных методов (GET, HEAD, OPTIONS)
                return request.method in permissions.SAFE_METHODS
        return False