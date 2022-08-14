from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images/")
    file = models.FileField(upload_to='songs/')