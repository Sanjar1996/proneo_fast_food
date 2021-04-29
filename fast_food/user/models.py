from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    tg_id = models.IntegerField(null=True)
    tg_user_name = models.CharField(null=True, max_length=40)
