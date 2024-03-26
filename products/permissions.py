from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    my_safe_method=['GET']
    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        else:
            return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in self.my_safe_method:
            return True
        return obj.user == request.user.is_staff