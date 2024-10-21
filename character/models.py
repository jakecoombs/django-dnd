from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class CharacterClass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
