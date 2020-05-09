from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CharacterForm
from .models import  Mission, Character

from . import function


def index(request):
    all_missions = Mission.objects.all()
    all_characters = Character.objects.all()
    context = {
        'all_missions': all_missions,
        'all_characters': all_characters,
    }
    return render(request, 'rpg/index.html', context)


def character_creation(request):

    form = CharacterForm()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            post = form
            check = post.save()
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
