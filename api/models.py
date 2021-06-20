from django.db import models
from users.models import User

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

'''
1. robię użytkownika - logowanie, 
                        wylogowywanie, 
                        lista użytkowników (permissions is supereuser)
                        widok pojedycznego użytkownika (tylko własne konto or is superuser)
2. pictures - na razie fulll
3. thumbnails
4. plany :
        musi być osobnym modelem i modelchoicefield - admin musi móc dodawać customowe
'''

def pics_dir_path(instance, filename):
    return 'pics/user_{0}/{1}'.format(instance.owner.uuid, filename)


def thumb_dir_path(instance, filename):
    return 'pics/user_{0}/thumb/{1}'.format(instance.owner.uuid, filename)


class Picture(models.Model):
    image = models.ImageField(upload_to=pics_dir_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    thumb = ThumbnailerImageField(upload_to=thumb_dir_path)

    saved_file.connect(generate_aliases_global)

#class Thumb(models.Model):
#    image = ThumbnailerImageField(upload_to=thumb_dir_path)
