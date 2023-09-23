from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
    path('how_to_play', views.how_to_play, name='how_to_play'),
    path('about', views.about, name='about'),
]