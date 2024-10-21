from django.urls import path

from . import views

app_name = "character"
urlpatterns = [
    path("", views.index, name="index"),
    path("character/", views.CharcterListView.as_view(), name="character_list"),
    path("character/<int:pk>/", views.CharacterDetailView.as_view(), name="character"),
    path("race/", views.RaceListView.as_view(), name="race_list"),
    path("race/<int:pk>/", views.RaceDetailView.as_view(), name="race"),
    path(
        "class/",
        views.CharacterClassListView.as_view(),
        name="characterclass_list",
    ),
    path(
        "class/<int:pk>/",
        views.CharacterClassDetailView.as_view(),
        name="characterclass",
    ),
]
