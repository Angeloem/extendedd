from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    girlfriend = models.CharField(max_length = 10,default = 'None')
    favorite = models.CharField(max_length = 10, default = 'None')

    def __str__(self):
        return self.email
