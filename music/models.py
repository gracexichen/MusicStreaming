from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    audio = models.FileField(upload_to="media")