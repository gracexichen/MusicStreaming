from django.forms import ModelForm
from django import forms
from .models import Songs

class UploadForm(ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'