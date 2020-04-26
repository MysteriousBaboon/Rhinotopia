from django.urls import path

from . import views

app_name = 'rpg'
urlpatterns = [
    path('', views.index, name='index'),
    path('character_creation', views.character_creation, name='character_creation'),
    path('Place', views.place_creation, name='place_creation'),
    path('<place_name>', views.detail_place, name='detail_place'),
    path('<character_name>', views.detail_character, name='character'),

]