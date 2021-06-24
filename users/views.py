from rest_framework import generics, permissions

from users.models import User
from users.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]




