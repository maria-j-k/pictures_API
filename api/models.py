import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from users.models import User


def pics_dir_path(instance, filename):
    return 'pics/user_{0}/{1}'.format(instance.owner.uuid, filename)


class Picture(models.Model):
    image = models.ImageField(upload_to=pics_dir_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=300,
        validators=[MinValueValidator(300), MaxValueValidator(30000)])

    def __str__(self):
        return f'{self.id}, {self.owner.email}'
    
    
    @property
    def expires(self):
        return  self.created + datetime.timedelta(
                seconds=self.duration)

    @property
    def valid(self):
        return self.expires >= timezone.now()

    @property
    def short_name(self):
        return self.image.name.split('/')[-1]


class Thumbnail(models.Model):
    url = models.URLField()
    picture = models.ForeignKey(Picture, 
            on_delete=models.CASCADE, 
            related_name='thumbnails')

    def __str__(self):
        return self.url

