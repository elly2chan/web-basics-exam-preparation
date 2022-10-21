from django.urls import path

from notes_app.notes.views import add_note, edit_note, delete_note, details_note

urlpatterns = (
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
)