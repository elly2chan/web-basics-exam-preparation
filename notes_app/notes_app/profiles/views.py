from django.shortcuts import render, redirect

from notes_app.notes.models import Note
from notes_app.profiles.models import Profile


def details_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.count()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'profiles/profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    profile.delete()
    notes.delete()
    return redirect('index')
