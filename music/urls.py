from django.urls import path
from starmusic import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #main webpage
    path('index', views.index, name='index'),
    path('addtoplaylist', views.addtoplaylist, name ='addtoplaylist'),
    path('new_playlist', views.new_playlist, name ='new_playlist'),
    path('upload', views.upload, name="upload"),
    #authentication
    path('', views.login_view, name="login"),
    path('signup', views.signup_view, name="signup"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.profile, name="profile"),
    path('<str:playlist_name>', views.playlist, name="playlist")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)