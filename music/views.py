from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Songs
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UploadForm

# Create your views here.
#main webpage
def index(request):
    songs = Songs.objects.all()
    return render(request, "music/index.html", {
        "songs": songs,
    })

def about(request):
    return render(request, "music/about.html")

def support(request):
    return render(request, "music/support.html")

def upload(request):
    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, "music/upload.html",context)

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
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "music/login.html", {
                "message": "Invalid credentials."
            })
    else:        
        return render(request, "music/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('browse'))
        else:
            return render(request, "music/about.html")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, "music/signup.html",context)