from django.urls import path

from . import views

app_name = 'rpg'
urlpatterns = [
    path('', views.index, name='index'),
    path('character/create/', views.character_creation, name='character_creation'),
    path('character/<int:character_id>/', views.character_detail, name='character_detail'),
    path('place/create/', views.place_creation, name='place_creation'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
]
