from django.shortcuts import render, redirect

from notes_app.notes.models import Note
from notes_app.profiles.forms import CreateProfileForm
from notes_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.all()
    notes = Note.objects.all()
    form = CreateProfileForm()

    context = {
        'profile': profile,
        'notes': notes,
        'form' : form,
    }

    if profile:
        return render(request, 'common/home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        return render(request, 'common/home-no-profile.html', context)
