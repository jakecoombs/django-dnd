from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from character.forms import CharacterModelForm
from character.models import Character, CharacterClass, Race


def index(request):
    recent_characters_list = Character.objects.order_by("-id").all()[:10]

    return render(
        request,
        "character/index.html",
        {"recent_characters_list": recent_characters_list},
    )


class CharcterListView(generic.ListView):
    template_name = "character/character_list.html"

    def get_queryset(self):
        """
        Return all characters.
        """
        return Character.objects.all()


class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = "character/character.html"


def create_character(request):
    if request.method == "POST":
        form = CharacterModelForm(request.POST)
        if form.is_valid():
            new_character = form.save()
            return HttpResponseRedirect(
                reverse("character:character", args=[new_character.id])
            )

    else:
        form = CharacterModelForm()

    return render(request, "character/character_create.html", {"form": form})


def edit_character(request, pk):
    instance = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharacterModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("character:character", args=[instance.id])
            )

    else:
        form = CharacterModelForm(instance=instance)

    return render(request, "character/character_edit.html", {"form": form, "pk": pk})


class CharacterClassDetailView(generic.DetailView):
    model = CharacterClass
    template_name = "character/characterclass.html"


class CharacterClassListView(generic.ListView):
    template_name = "character/characterclass_list.html"

    def get_queryset(self):
        """
        Return all character classes.
        """
        return CharacterClass.objects.order_by("name").all()


class RaceListView(generic.ListView):
    template_name = "character/race_list.html"

    def get_queryset(self):
        """
        Return all races.
        """
        return Race.objects.order_by("name").all()


class RaceDetailView(generic.DetailView):
    model = Race
    template_name = "character/race.html"
