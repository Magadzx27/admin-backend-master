from rest_framework import permissions

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        else:
            return request.user and request.user.is_staff