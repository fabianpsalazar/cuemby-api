from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin


class Teams(models.Model):
    page = models.IntegerField(null=True)
    total_pages = models.IntegerField(null=True)
    items = models.IntegerField(null=True)
    total_items = models.IntegerField(null=True)

    
class Players(models.Model):
    name = models.CharField(max_length=100) 
    position = models.CharField(max_length=5)
    nation = models.CharField(max_length=100)
    club = models.CharField(max_length=100, null=True)