from django.shortcuts import render

from gamesplay_app.games.models import Game
from gamesplay_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'common/home-page.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games
    }

    return render(request, 'common/dashboard.html', context)
