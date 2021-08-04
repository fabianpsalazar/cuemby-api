from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.
class User(AbstractUser):
    pass 

class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    page = models.IntegerField()
    total_pages = models.IntegerField()
    items = models.IntegerField()
    total_items = models.IntegerField()
    
class Players(models.Model):
    players_id = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name='related players')
    name = models.CharField(max_length=100) 
    position = models.CharField(max_length=5)
    nation = models.CharField(max_length=20)