from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User


def pics_dir_path(instance, filename):
    return 'pics/user_{0}/{1}'.format(instance.owner.uuid, filename)


class Picture(models.Model):
    image = models.ImageField(upload_to=pics_dir_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.IntegerField(default=300,
        validators=[MinValueValidator(300), MaxValueValidator(30000)])

    def __str__(self):
        return f'{self.id}, {self.owner.email}'


class Thumbnail(models.Model):
    url = models.URLField()
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='thumbnails')

    def __str__(self):
        return self.url

