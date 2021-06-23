from django.core.management.base import BaseCommand 
from easy_thumbnails.files import get_thumbnailer

from api.models import Thumbnail

class Command(BaseCommand): 
    help = 'Destroys thumbnails when expired'

    def handle(self, *args, **kwargs):
        expired = Thumbnail.objects.expired()
        thumbnails = [item.pk for item in expired]
        for item in expired:
            thumbmanager = get_thumbnailer(item.image)
            thumbmanager.delete_thumbnails()
        expired.delete()
        self.stdout.write('Succesfully deleted {}'.format(thumbnails))

