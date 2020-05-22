from django.urls import path


from . import views

app_name = 'rpg'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('character/create/', views.character_creation, name='character_creation'),
    path('character/<int:character_id>/', views.character_detail, name='character_detail'),
    path('mission/<int:mission_id>/', views.mission_detail, name='mission_detail'),
    path('mission/success/<int:character_id>/', views.mission_success, name='mission_success'),
]
