from django.urls import path

from . import views

app_name = 'rpg'
urlpatterns = [
    path('', views.index, name='index'),
    path('<place_name>', views.detail_place, name='detail_place'),
    path('<character_name>', views.detail_character, name='character'),

]