from django import forms

from character.models import CharacterClass, Race


class CharacterForm(forms.Form):
    name = forms.CharField(label="Character's name", max_length=50)
    race = forms.ChoiceField(choices={i: i for i in Race.objects.all()})
    character_class = forms.ChoiceField(
        choices={i: i for i in CharacterClass.objects.all()}
    )
    level = forms.IntegerField(min_value=1)
