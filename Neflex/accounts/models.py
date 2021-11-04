from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, TextField

# Create your models here.

class User(AbstractUser):
    # like_movie = TextField(blank=True)
    pass

class UserTaste(models.Model):
    user_Id = models.IntegerField()
    user_movie = models.IntegerField()

