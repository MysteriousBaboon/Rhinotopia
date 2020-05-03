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
            post.save()
            return redirect('rpg:index')

    return render(request, 'rpg/character_creation.html', {'form': form})


def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'rpg/character_detail.html', {'character': character})


def mission_detail(request, mission_id):
    mission = get_object_or_404(Mission, id=mission_id)

    if request.method == 'POST':
        if function.calculating_sucess(mission.sucess):
            return render(request, 'rpg/index.html')
        else:
            return redirect('rpg:index')

    return render(request, 'rpg/mission_detail.html', {'mission': mission})
