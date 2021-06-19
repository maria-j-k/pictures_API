import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import UserManager
'''
w plikach statycznych mam obrazki
użytkownik może ściągnąć do siebie na komputer obrazek
użytkownikowi w profilu powinna się wyświetlać lista obrazków, które ściągnął (tylko nazwy, bez linków)

1. robię użytkownika - logowanie, 
                        wylogowywanie, 
                        lista użytkowników (permissions is supereuser)
                        widok pojedycznego użytkownika
2. plan musi być osobnym modelem i modelchoicefield - admin musi móc dodawać customowe

'''
class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


