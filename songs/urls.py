from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("songs", views.songs, name="songs"),
    path("songs/<int:song_id>", views.song, name="song"),
    path("songs/new", views.new, name="new"),
    path("<int:song_id>/edit", views.edit, name="edit"),
    path("groups", views.groups, name="groups"),
    path("groups/<int:group_id>", views.grouplist, name="grouplist")
]