from django import forms


class CharacterForm(forms.Form):
    name = forms.CharField(label="Character's name", max_length=50)
