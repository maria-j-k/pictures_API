from rest_framework import permissions

class IsThemself(permissions.BasePermission):
    message="Not your account"
    
    def has_object_permission(self, request, view, obj):
        print(f'obj is {obj}')
        print(f'request.user is {request.user}')
        return request.user == obj


