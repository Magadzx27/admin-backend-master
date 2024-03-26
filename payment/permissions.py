from rest_framework import permissions
from orders.models import Orders


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            order_id = request.data.get('order_id')
            instance = Orders.objects.get(pk=order_id)
            return instance.user_id == request.user 
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # return true for object owner or user staff, and false for anyone else 
        if obj.user_id == request.user :
            
            return True
        
        else:
            return request.user and request.user.is_staff
        

        