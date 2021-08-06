from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin

class Players(models.Model):
    name = models.CharField(max_length=100) 
    position = models.CharField(max_length=5)
    nation = models.CharField(max_length=100)
    club = models.CharField(max_length=100, null=True)