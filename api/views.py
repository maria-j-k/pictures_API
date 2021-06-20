from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser


from api.models import Picture
from api.serializers import PictureSerializer


class PictureViewSet(viewsets.ModelViewSet):
    model = Picture
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Picture.objects.all()
        return Picture.objects.filter(owner=user)

    #TODO
    # dopisać filtr po użytkowniku:w

