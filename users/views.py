from rest_framework import generics, permissions

from users.models import User
from users.serializers import UserSerializer
from users import permissions as custom

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [custom.IsThemself | permissions.IsAdminUser]

'''
login przekierowuje na /users/
    powinien na users/<user_id>/
    dać do UserList jako action?
'''


