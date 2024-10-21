from django.contrib import admin

from .models import Character, CharacterClass, Race

admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(Race)
