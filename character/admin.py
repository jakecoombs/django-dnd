from django.contrib import admin

from .models import Character, CharacterClass, Race


class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "race", "character_class"]}),
        ("Stats", {"fields": ["level", "armor_class", "hit_points"]}),
        (
            "Abilities",
            {
                "fields": [
                    "strength",
                    "dexterity",
                    "constitution",
                    "intelligence",
                    "wisdom",
                    "charisma",
                ]
            },
        ),
    )
    search_fields = ("name",)


class CharacterClassAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class RaceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ["name", "parent_race", "description"]}),
        ("Stats", {"fields": ["size", "speed"]}),
    )
    search_fields = ("name",)


admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterClass, CharacterClassAdmin)
admin.site.register(Race, RaceAdmin)
