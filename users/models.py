from django.db import models

# Create your models here.
from django.utils import timezone

# USE MATTS SHIT

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.TextField()
    email = models.TextField()