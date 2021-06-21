from rest_framework import permissions

class IsThemself(permissions.BasePermission):
    message="Not your account"
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj


