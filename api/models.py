from django.db import models
from users.models import User

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

class Picture(models.Model):
    image = models.ImageField(upload_to=pics_dir_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


