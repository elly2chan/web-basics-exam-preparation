from django.shortcuts import render, redirect

from music_app.albums.models import Album
from music_app.profiles.forms import CreateProfileForm
from music_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()

    if profile:
        albums = Album.objects.all()
        context = {
            'profile': profile,
            'albums': albums,
        }
        return render(request, 'common/home-with-profile.html', context)
    else:
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

    return render(request, 'common/home-no-profile.html', context)
