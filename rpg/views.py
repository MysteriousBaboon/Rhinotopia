from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

from .models import Place


def index(request):
    latest_place_list = Place.objects.order_by('place_name')[:5]
    context = {
        'latest_place_list': latest_place_list,
    }
    return render(request, 'rpg/index.html', context)


def character_creation(request):
    return render(request, 'rpg/character_creation.html')


def character_detail(request, character_name):
    return HttpResponse("You're are %s." % character_name)


def place_creation(request):
    return render(request, 'rpg/place_creation.html')


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return render(request, 'rpg/place_detail.html', {'place': place})
