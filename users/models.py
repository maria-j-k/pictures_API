import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import UserManager
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
    expiring_links = models.BooleanField()
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

