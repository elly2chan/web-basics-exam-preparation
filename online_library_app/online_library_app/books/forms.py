from django import forms

from online_library_app.books.models import Book


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AddBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass

