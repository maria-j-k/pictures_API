from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser


from api.models import Picture, Thumbnail
from api.serializers import PictureSerializer, ThumbnailSerializer


class PictureViewSet(viewsets.ModelViewSet):
    model = Picture
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(owner=user)


class ProfileViewSet(viewsets.ModelViewSet):
    model = Thumbnail
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Thumbnail.objects.filter(picture__owner=user)


class ThumbnailView():
    pass
