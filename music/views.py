from django.shortcuts import render
from .models import Songs

# Create your views here.
def index(request):
    return render(request, "music/index.html")

def about(request):
    return render(request, "music/about.html")

def support(request):
    return render(request, "music/support.html")

def browse(request):
    songs = Songs.objects.all()
    return render(request, "music/browse.html", {
        "songs": songs,
    })

