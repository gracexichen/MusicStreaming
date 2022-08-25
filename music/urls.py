from django.urls import path
from starmusic import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #main webpage
    path('index', views.index, name='index'),
    path('upload', views.upload, name="upload"),
    #authentication
    path('signup', views.signup_view, name="signup"),
    path('', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.profile, name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)