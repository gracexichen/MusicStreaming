from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Songs
from django.contrib.auth import authenticate,login,logout

# Create your views here.
#main webpage
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

#authentication
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "music/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "music/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "music/login.html")

def logout_view(request):
    logout(request)
    return render(request, "music/login.html", {
        "message": "Logged out."
    })