from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Songs


class UploadForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['title', 'image', 'audio']
        