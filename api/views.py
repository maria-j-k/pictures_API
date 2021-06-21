from rest_framework import generics, permissions, viewsets
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


class ThumbnailView(generics.RetrieveAPIView):
    model = Thumbnail
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer
#    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'url'


    def get_queryset(self):
        user = self.request.user
        return Thumbnail.objects.filter(picture__owner=user)

    def get(self, request, **kwargs):
        print('geting')
        self.object = self.get_object()
        print(self.object)
        if self.request.path != self.object.get_absolute_url():
            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


