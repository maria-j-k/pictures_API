from django.http import FileResponse
from rest_framework import generics, permissions, views, viewsets, renderers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Picture, Thumbnail
from users.models import ThumbSize
from api import serializers


class PictureCreateView(generics.CreateAPIView):
    model = Picture
    queryset = Picture.objects.all()
    serializer_class = serializers.PictureCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)


class PictureListView(generics.ListAPIView):
    model = Picture
    queryset = Picture.objects.all()
    serializer_class = serializers.PictureListSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)

class ThumbnailView(generics.CreateAPIView):
    model = Thumbnail
    queryset = Thumbnail.objects.all()
    serializer_class = serializers.ThumbnailSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]


    def get_serializer_context(self):
        context = super().get_serializer_context()
        print(f'get context: {context}')
        picture = Picture.objects.get(pk=self.kwargs['pic_pk'])
        size = ThumbSize.objects.get(pk=self.kwargs['size_pk'])
        context['size'] = size
        context['picture'] = picture
        print(f'After changes: get context: {context}')
        return context

#    def perform_create(self, serializer):
#        picture = Picture.objects.get(pk=self.kwargs['pic_pk'])
#        size = ThumbSize.objects.get(pk=self.kwargs['size_pk'])
#        print(f'size is {size.name}, {size.size}')
#        serializer.save(picture=picture, size=size)
