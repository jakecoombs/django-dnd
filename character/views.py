from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from character.forms import CharacterModelForm
from character.models import Character, CharacterClass, Race


def index(request):
    return render(request, "character/index.html")


class CharcterListView(generic.ListView):
    template_name = "character/character_list.html"

    def get_queryset(self):
        """
        Return all characters.
        """
        return Character.objects.all()


class CharacterDetailView(generic.DetailView):
    model = Race
    template_name = "character/character.html"


def create_character(request):
    if request.method == "POST":
        form = CharacterModelForm(request.POST)
        if form.is_valid():
            # TODO: Create character with `form.cleaned_data`
            return HttpResponseRedirect(reverse("character:character_list"))

    else:
        form = CharacterModelForm()

    return render(request, "character/character_create.html", {"form": form})


class CharacterClassDetailView(generic.DetailView):
    model = CharacterClass
    template_name = "character/characterclass.html"


class CharacterClassListView(generic.ListView):
    template_name = "character/characterclass_list.html"

    def get_queryset(self):
        """
        Return all character classes.
        """
        return CharacterClass.objects.all()


class RaceListView(generic.ListView):
    template_name = "character/race_list.html"

    def get_queryset(self):
        """
        Return all races.
        """
        return Race.objects.all()


class RaceDetailView(generic.DetailView):
    model = Race
    template_name = "character/race.html"
