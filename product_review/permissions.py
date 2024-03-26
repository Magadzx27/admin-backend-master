from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    my_safe_method=['GET']
    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        else:
            return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj.user_id == request.user:
            return True
        else:
            return request.user and request.user.is_staff