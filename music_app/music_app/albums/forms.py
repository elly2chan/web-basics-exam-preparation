from django import forms

from music_app.albums.mixins import DisableFormFields
from music_app.albums.models import Album


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name', }),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist', }),
            'description': forms.Textarea(attrs={'placeholder': 'Description', }),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL', }),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', }),
        }


class CreateAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(DisableFormFields, BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()
