from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class CharacterClass(models.Model):
    name = models.CharField(max_length=50)

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
