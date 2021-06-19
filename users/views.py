from rest_framework import generics
from rest_framework import permissions

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


admin = '93ff9c3b-a618-4cb2-b445-0128085e48ab'
maria = '53c1ae73-2502-4a70-878d-601d168a42b4'
