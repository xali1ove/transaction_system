from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Client(AbstractBaseUser):
    username = models.CharField(max_length=64, default='')
    balance_value = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.username
