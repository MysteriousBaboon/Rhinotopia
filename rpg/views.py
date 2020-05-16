from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import CharacterForm
from .models import  Mission, Character

from . import function


def index(request):
    all_missions = Mission.objects.all()
    all_characters = Character.objects.all()

    context = {
        'all_missions': all_missions,
        'all_characters': all_characters,
        'log_status': request.user.is_authenticated,
    }
    return render(request, 'rpg/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'rpg/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            print("fuck")
    else:
        return render(request, 'rpg/login.html')


def character_creation(request):

    form = CharacterForm()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            post = form
            post.save()
            return redirect('rpg:index')

    return render(request, 'rpg/character_creation.html', {'form': form, 'character': Character})


def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    if request.method == 'POST':
        if character.available_point > 0:
            if 'strength' in request.POST:
                character.strength += 1
                character.available_point -= 1
            if 'agility' in request.POST:
                character.agility += 1
                character.available_point -= 1
            if 'intelligence' in request.POST:
                character.intelligence += 1
                character.available_point -= 1

    character.race = character.specie
    character.save()

    return render(request, 'rpg/character_detail.html', {'character': character, 'point_available': character.available_point})


def mission_detail(request, mission_id):
    mission = get_object_or_404(Mission, id=mission_id)
    characters = Character.objects.all()
    context = {
        'mission': mission,
        'characters': characters,
    }

    if request.method == 'POST':
        character_id = request.POST['characters']
        character = Character.objects.get(id=character_id)

        character.isOccupied = True
        character.save()

        context = {
            'success': function.calculating_sucess(mission, character),
            'character': character,
        }

        return render(request, 'rpg/mission_finish.html', context)


    return render(request, 'rpg/mission_detail.html', context)
