from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=64, unique=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    audio = models.FileField(upload_to="media")
    likes = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="media")

    def __str__(self):
        return self.user.username

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    song = models.ManyToManyField(Songs, blank=True)

    def __str__(self):
        return self.name