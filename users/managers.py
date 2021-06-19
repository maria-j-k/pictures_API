import uuid

from django.db import models
from django.contrib.auth.models import BaseUserManager


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

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


