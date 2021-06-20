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
class ThumbSize(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()

    @property
    def dimensions(self):
        return {'size': (self.size, self.size)}
    
    def __str__(self):
        return f'{self.name}: {self.size}x{self.size}'


class Plan(models.Model):
    name = models.CharField(max_length=100)
    original = models.BooleanField()
    exipring_links = models.BooleanField()
    thumbsizes = models.ManyToManyField(ThumbSize)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

