from django.db import models
from django.urls import reverse

class andouuser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    account = models.FloatField()
    address = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)


def __str__(self):
    return self.username
