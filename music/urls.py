from django.urls import path
from starmusic import settings
from django.conf.urls.static import static
from . import views

app_name = "music"
urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('browse', views.browse, name='browse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
