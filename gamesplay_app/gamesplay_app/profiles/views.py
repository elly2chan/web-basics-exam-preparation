from django.shortcuts import render, redirect

from gamesplay_app.games.models import Game
from gamesplay_app.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from gamesplay_app.profiles.models import Profile


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    average_rating = sum([game.rating for game in games]) / len(games)

    context = {
        'profile': profile,
        'games': games,
        'average_rating': average_rating,
    }

    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    form = DeleteProfileForm()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/delete-profile.html', context)
