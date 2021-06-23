from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.alias import aliases
from users.models import User


def pics_dir_path(instance, filename):
    return 'pics/user_{0}/{1}'.format(instance.owner.uuid, filename)


def thumbs_dir_path(instance, filename):
    return 'pics/user_{0}/{1}'.format(instance.picture.image.owner.uuid, filename)


class Picture(models.Model):
    image = models.ImageField(upload_to=pics_dir_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.owner.email}'
    
    

    @property
    def short_name(self):
        return self.image.name.split('/')[-1]

    @property
    def sizes(self):
        return self.owner.plan.thumbsizes.all()


class ThumbnailManager(models.Manager):
    def create(self, *args, **kwargs):
        link_validity = kwargs['link_validity']
        picture = kwargs['picture']
        expires = timezone.now() + timedelta(seconds=link_validity)
        size = kwargs['size']
        options = {'crop': True}
        options.update(size.dimensions)
        if not aliases.get(size.name):
            aliases.set(size.name, options)
        thumbnailer = get_thumbnailer(picture.image)

        return super(ThumbnailManager, self).create(
                expires=expires, 
                picture_id=picture.id, 
                image=thumbnailer, 
                link_validity=link_validity)
    
    def expired(self):
        return self.filter(expires__lte=timezone.now())

    

class Thumbnail(models.Model):
    expires = models.DateTimeField()
    image = ThumbnailerImageField(upload_to=thumbs_dir_path)
    link_validity =  models.IntegerField(default=300,
        validators=[MinValueValidator(300), MaxValueValidator(30000)])

    picture = models.ForeignKey(Picture, 
            on_delete=models.CASCADE, 
            related_name='thumbnails')
    objects = ThumbnailManager()


    @property
    def sizes(self):
        return self.picture.owner.plan.thumbsizes.all()


    @property
    def valid(self):
        return self.expires >= timezone.now()
    
    def __str__(self):
        return self.image.name


