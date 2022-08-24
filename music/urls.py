from django.urls import path
from starmusic import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #main webpage
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('browse', views.browse, name='browse'),
    path('upload', views.upload, name="upload"),
    #authentication
    path('signup', views.signup_view, name="signup"),
    path('', views.login_view, name="login"),
    path('home', views.home, name="home"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.profile, name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)