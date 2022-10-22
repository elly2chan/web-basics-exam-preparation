from django.shortcuts import render, redirect

from music_app.albums.models import Album
from music_app.profiles.forms import DeleteProfileForm
from music_app.profiles.models import Profile


def details_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.count()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = DeleteProfileForm()

    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'albums': albums,
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)
