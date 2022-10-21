from django.shortcuts import render, redirect

from notes_app.notes.forms import AddNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.notes.models import Note


def add_note(request):
    if request.method == 'GET':
        form = AddNoteForm()
    else:
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'notes/note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'notes/note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':

        context = {
            'note': note,
            'form': DeleteNoteForm(instance=note),
        }

        return render(request, 'notes/note-delete.html', context)
    else:
        note.delete()
        return redirect('index')


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    context = {
        'note': note
    }

    return render(request, 'notes/note-details.html', context)
