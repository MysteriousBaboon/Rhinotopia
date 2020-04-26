from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404


from .models import Place


# Create your views here.
def index(request):
    latest_place_list = Place.objects.order_by('place_name')[:5]
    context = {
        'latest_place_list': latest_place_list,
    }
    return render(request, 'rpg/index.html', context)


def character_creation(request):
    return render(request, 'rpg/character_creation.html')


def place_creation(request):
    return render(request, 'rpg/place_creation.html')


def detail_place(request, place_name):
    place = get_object_or_404(Place, place_name=place_name)
    return render(request, 'rpg/detail_place.html', {'place': place})


def detail_character(request, character_name):
    return HttpResponse("You're are %s." %character_name)