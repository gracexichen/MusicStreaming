from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "music/index.html")

def about(request):
    return render(request, "music/about.html")

def support(request):
    return render(request, "music/support.html")