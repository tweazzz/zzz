from rest_framework import permissions

class IsAdminSchool(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.is_anonymous:
            return request.method in permissions.SAFE_METHODS
        elif request.user.is_authenticated and request.user.role == 'admin':
            return request.user.school_id == request.user.school_id
        return False

class IsSuperAdminOrReadOnly(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False