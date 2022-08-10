from django.urls import path
from . import views

app_name = "music"
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('browse', views.browse, name='browse')
]