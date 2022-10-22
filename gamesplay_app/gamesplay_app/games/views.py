from django.shortcuts import render, redirect

from gamesplay_app.games.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app.games.models import Game
from gamesplay_app.profiles.models import Profile


def create_game(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'games/create-game.html', context)


def details_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'game': game,
    }

    return render(request, 'games/details-game.html', context)


def edit_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/edit-game.html', context)


def delete_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.filter(pk=pk).get()
    form = DeleteGameForm(instance=game)

    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/delete-game.html', context)

