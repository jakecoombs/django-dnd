from django import forms

from character.models import Character, CharacterClass, Race


class CharacterForm(forms.Form):
    name = forms.CharField(label="Character's name", max_length=50)
    race = forms.ChoiceField(choices={i: i for i in Race.objects.all()})
    character_class = forms.ChoiceField(
        choices={i: i for i in CharacterClass.objects.all()}
    )
    level = forms.IntegerField(min_value=1)


class CharacterModelForm(forms.ModelForm):
    race = forms.ModelChoiceField(Race.objects.order_by("name"))
    character_class = forms.ModelChoiceField(CharacterClass.objects.order_by("name"))

    class Meta:
        model = Character
        fields = (
            "name",
            "race",
            "character_class",
            "level",
            "armor_class",
            "hit_points",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        )
