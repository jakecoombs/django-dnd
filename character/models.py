from django.db import models
from django.utils.translation import gettext_lazy as _


class Race(models.Model):
    class Size(models.TextChoices):
        TINY = "TY", _("Tiny")
        SMALL = "SM", _("Small")
        MEDIUM = "MD", _("Medium")
        LARGE = "LG", _("Large")
        HUGE = "HG", _("Huge")
        GARGANTUAN = "GT", _("Gargantuan")

    name = models.CharField(max_length=50, unique=True)
    parent_race = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="subraces"
    )
    description = models.TextField()
    size = models.CharField(max_length=2, choices=Size.choices, default=Size.MEDIUM)
    speed = models.IntegerField(default=30)

    def __str__(self) -> str:
        return self.name


class CharacterClass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    armor_class = models.IntegerField()
    hit_points = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    def __str__(self) -> str:
        return self.name
