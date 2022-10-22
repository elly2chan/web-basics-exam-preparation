from django.shortcuts import render, redirect

from music_app.albums.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from music_app.albums.models import Album
from music_app.profiles.models import Profile


def add_album(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'albums/add-album.html', context)


def details_album(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(pk=pk)
    form = DeleteAlbumForm(instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
        'album': album,
    }

    return render(request, 'albums/delete-album.html', context)
