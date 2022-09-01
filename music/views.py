from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Songs, Profile, Playlist
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UploadForm, ProfileForm
import Image
import json


# Create your views here.
profilepic = "/static/music/icons/user.png"

def findProfile(request):
    global profilepic
    for profile in Profile.objects.all():
        if profile.user == request.user:
            profilepic = profile.profilepic.url
def index(request):
    songs = Songs.objects.all()
    playlists = Playlist.objects.filter(user=request.user)
    profilepic = "/static/music/icons/user.png"
    songnames = []

    for song in Songs.objects.all():
        songnames.append(song.title + " by " + song.artist.username)

    for profile in Profile.objects.all():
        if profile.user == request.user:
            profilepic = profile.profilepic.url

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        id = request.POST.get('button_value')
        if id=="":
            return JsonResponse({{"likes": None}},status=200)
        object = Songs.objects.get(pk=id)
        object.likes += 1
        object.save()
        numLikes = object.likes
        return JsonResponse({'likes': numLikes},status=200)
    else:
        return render(request, "music/index.html", {
            "songs": songs,
            "songnames": songnames,
            "profilepic": profilepic,
            "playlists": playlists,
        })

def contact(request):
    findProfile(request)
    
    return render(request, "music/contact.html", {
        "profilepic": profilepic,
    })

def addtoplaylist(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        playlist_name = request.POST.get('playlist_name')
        song_ID = request.POST.get("song_ID")
        user = request.user
        playlist = Playlist.objects.get(user=user, name=playlist_name)
        add_song = Songs.objects.get(pk=song_ID)
        playlist.song.add(add_song)
        playlist.save()
    return JsonResponse({'playlist':playlist_name}, status=200)

def new_playlist(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        playlist_name = request.POST.get('new_playlist')
        new = Playlist.objects.create(user=request.user, name=playlist_name)
        new.save()
    return JsonResponse({'newPlaylist',playlist_name}, status=200)

def upload(request):
    findProfile(request)

    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.artist = request.user
            obj.likes = 0
            obj.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UploadForm()
    context = {
        'form': form,
        "profilepic": profilepic
        }
    return render(request, "music/upload.html",context)

def playlist(request, playlist_name):

    title = []
    artist = []
    image = []
    audio = []
    description = []
    playlists = Playlist.objects.all()
    try:
        playlist = Playlist.objects.get(name=playlist_name)

        songs = playlist.song.all()
        for song in songs:
            title.append(song.title)
            artist.append(song.artist.username)
            image.append(song.image.url)
            audio.append(song.audio.url)
            description.append(song.description)

        titlelist = json.dumps(title)
        artistlist = json.dumps(artist)
        imagelist = json.dumps(image)
        audiolist = json.dumps(audio)
        descriptionlist= json.dumps(description)

        return render(request, "music/playlist.html", {
            "playlists": playlists,
            "playlist": playlist,
            "songs": songs,
            "title": titlelist,
            "artist": artistlist,
            "image":imagelist,
            "audio": audiolist,
            "description": descriptionlist,
        })
    except Playlist.DoesNotExist:
        return render(request, "music/index.html")


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
    findProfile(request)

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
        "form": form,
        "profilepic": profilepic,
    }
    return render(request, "music/profile.html", context)