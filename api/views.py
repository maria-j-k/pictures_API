from django.http import FileResponse
from rest_framework import generics, permissions, views, viewsets, renderers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Picture, Thumbnail
from api.serializers import PictureSerializer, ThumbnailSerializer


class PictureView(generics.ListCreateAPIView):
    model = Picture
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)


