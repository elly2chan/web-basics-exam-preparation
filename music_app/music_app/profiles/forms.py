from django import forms

from music_app.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ()
