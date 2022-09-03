from django.contrib import admin
from .models import Songs, Profile, Playlist, Comment
# Register your models here.
admin.site.register(Songs)
admin.site.register(Profile)
admin.site.register(Playlist)
admin.site.register(Comment)