from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Songs, Profile


class UploadForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['title', 'image', 'audio']
        
class ProfileForm(ModelForm, forms.Form):
    profilepic = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['profilepic']