import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from users.models import User


def pics_dir_path(instance, filename):
    return 'pics/user_{0}/{1}'.format(instance.owner.uuid, filename)


def thumbs_dir_path(instance, filename):
    return 'pics/user_{0}/thumbnails/{1}'.format(instance.picture.image.owner.uuid, filename)


class Picture(models.Model):
    image = models.ImageField(upload_to=pics_dir_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}, {self.owner.email}'
    
    

    @property
    def short_name(self):
        return self.image.name.split('/')[-1]

    @property
    def sizes(self):
        return self.owner.plan.thumbsizes.all()


class Thumbnail(models.Model):
    image = ThumbnailerImageField(upload_to=thumbs_dir_path)
    link_validity =  models.IntegerField(default=300,
        validators=[MinValueValidator(300), MaxValueValidator(30000)])

    picture = models.ForeignKey(Picture, 
            on_delete=models.CASCADE, 
            related_name='thumbnails')
    url = models.URLField(blank=True, null=True)

    @property
    def sizes(self):
        return self.picture.owner.plan.thumbsizes.all()

    
    @property
    def expires(self):
        return  self.picture.created + datetime.timedelta(
                seconds=self.duration)

    @property
    def valid(self):
        return self.expires >= timezone.now()
    
    def __str__(self):
        return self.image.name

