from django.urls import path
from . import views
urlpatterns = [
    path("", views.lobbyHome, name="Lobby Home"),
]