from django.shortcuts import render, redirect

from online_library_app.books.models import Book
from online_library_app.profiles.forms import CreateProfileForm
from online_library_app.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()
    books = Book.objects.all()
    form = CreateProfileForm()

    context = {
        'form': form,
        'profile': profile,
        'books': books,
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

