from django.contrib import admin

from .models import Character, CharacterClass, Race


class RaceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "parent_race", "description"]}),
        ("Stats", {"fields": ["size", "speed"]}),
    )
    search_fields = ("name",)


admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(Race, RaceAdmin)
