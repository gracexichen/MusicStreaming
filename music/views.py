from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Songs, Profile, Playlist
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UploadForm, ProfileForm

# Create your views here.
#main webpage
def index(request):
    songs = Songs.objects.all()
    playlist = Playlist.objects.all()
    profilepic = "/static/music/icons/user.png"
    songnames = []
    for song in Songs.objects.all():
        songnames.append(song.title + " by " + song.artist.username)

    for profile in Profile.objects.all():
        if profile.user == request.user:
            profilepic = profile.profilepic.url

    return render(request, "music/index.html", {
        "songs": songs,
        "songnames": songnames,
        "profilepic": profilepic,
        "playlist": playlist,
    })

def upload(request):
    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.artist = request.user
            obj.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, "music/upload.html",context)

#authentication
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
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('signup'))
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, "music/signup.html",context)

def profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            HttpResponseRedirect(reverse('index'))
    else:
        form = ProfileForm()
    context = {
        "form": form
    }
    return render(request, "music/profile.html", context)