from datetime import datetime, timezone

from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import CharacterForm
from .models import Mission, Character

from . import function
from .function import log_check as log_status


def index(
        request):  # Handling the Index, display every character associated with the profile or otherwise return a tuto
    log = log_status(request)
    characters_finish = []
    mission_list = None
    if log:
        for character in Character.objects.filter(isOccupied=True, owner_id=request.user.id):
            if character.finishTime < datetime.now(timezone.utc):
                characters_finish.append(character)

        if not request.user.profile.missions_access:  # TODO need to find a way to storethe missions in the profile so it doesn't load differents missions each time you go to index
            mission_list = function.mission_selection(request)
            request.user.profile.missions_access = mission_list
        else:
            pass

    all_characters = Character.objects.filter(owner_id=request.user.id)
    context = {
        'all_missions': mission_list,
        'log_status': log,
        'all_characters': all_characters,
        'characters_finish': characters_finish,
    }
    return render(request, 'rpg/index.html', context)


def signup(request):  # Handling signup using a form
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


def logout_view(request):  # Log Out
    logout(request)
    return redirect('/')


def login_view(request):  # Handling Login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            print("fuck")  # TODO make an error display messaage
    else:
        return render(request, 'rpg/login.html')


@login_required(login_url='/')
def character_creation(request):  # Use a form to create a character, add 1 to the number of character

    form = CharacterForm()
    if request.method == 'POST':
        if request.user.profile.character_number < request.user.profile.character_number_max:
            form = CharacterForm(request.POST)
            if form.is_valid():
                post = form
                character = post.save()
                character.owner_id = request.user.id
                character.save()
                request.user.profile.character_number += 1
                request.user.save()
                return redirect('rpg:index')
        else:
            # TODO Error
            print("error")

    return render(request, 'rpg/character_creation.html', {'form': form, 'character': Character,
                                                           'log_status': log_status(request)})


@login_required(login_url='/')
def character_detail(request,
                     character_id):  # Check the character sheet ,if it has available skill point buttons will be displayed to upgrade stats
    character = get_object_or_404(Character, id=character_id)
    if request.method == 'POST':
        if character.available_point > 0:
            if 'strength.x' in request.POST:
                character.strength += 1
                character.available_point -= 1
            if 'agility.x' in request.POST:
                character.agility += 1
                character.available_point -= 1
            if 'intelligence.x' in request.POST:
                character.intelligence += 1
                character.available_point -= 1

    character.race = character.specie
    character.save()

    return render(request, 'rpg/character_detail.html', {'character': character,
                                                         'point_available': character.available_point,
                                                         'is_owner': request.user.id == character.owner_id,
                                                         'log_status': log_status(request),
                                                         })


@login_required(login_url='/')
def mission_detail(request, mission_id):
    mission = get_object_or_404(Mission, id=mission_id)
    characters = Character.objects.filter(owner_id=request.user.id, isOccupied=False)

    context = {
        'mission': mission,
        'characters': characters,
        'log_status': log_status(request),
    }

    if request.method == 'POST':
        character_id = request.POST['characters']
        character = Character.objects.get(id=character_id)
        function.sendmission(character, mission)

        context = {
            'log_status': log_status(request),
        }

        return redirect('/')

    return render(request, 'rpg/mission_detail.html', context)


@login_required(login_url='/')
def mission_success(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    success = function.resultmission(character)

    context = {'log_status': log_status(request),
               'success': success,
               }
    return render(request, 'rpg/mission_success.html', context)
