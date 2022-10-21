from django.shortcuts import render, redirect

from online_library_app.books.models import Book
from online_library_app.profiles.forms import EditProfileForm, DeleteProfileForm
from online_library_app.profiles.models import Profile


def details_profile(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


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
    books = Book.objects.all()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        profile.delete()
        books.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
        'books': books,
    }

    return render(request, 'profiles/delete-profile.html', context)
