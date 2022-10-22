from django import forms

from gamesplay_app.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput()
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ()
