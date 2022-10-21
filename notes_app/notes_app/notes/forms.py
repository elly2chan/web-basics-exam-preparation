from django import forms

from notes_app.notes.mixins import DisableFormFields
from notes_app.notes.models import Note


class BaseNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class AddNoteForm(BaseNoteForm):
    pass


class EditNoteForm(BaseNoteForm):
    pass


class DeleteNoteForm(DisableFormFields, BaseNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()
