from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):

    def __str__(self):
        return self.first_name+" "+self.last_name
class Music(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    audio_file = models.FileField(upload_to='musics/')
    cover_image = models.ImageField(upload_to='music_image/')

    def __str__(self):
        return self.title

    class META:
        ordering = ["title"]



