from django.views import generic

from character.models import Character


class IndexView(generic.ListView):
    template_name = "character/index.html"

    def get_queryset(self):
        """
        Return all characters.
        """
        return Character.objects.all()


class DetailView(generic.DetailView):
    model = Character
    template_name = "character/detail.html"
