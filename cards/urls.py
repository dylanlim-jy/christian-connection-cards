from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
    path('how-to-play', views.how_to_play, name='how_to_play'),
    path('about', views.about, name='about'),
    path('suggest', views.suggest, name='suggest'),
    path('question-bank', views.question_bank, name='question_bank'),
]