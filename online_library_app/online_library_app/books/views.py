from django.shortcuts import render, redirect

from online_library_app.books.forms import AddBookForm, EditBookForm
from online_library_app.books.models import Book


def add_book(request):
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'books/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'books/edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
    }

    return render(request, 'books/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    book.delete()
    return redirect('index')
