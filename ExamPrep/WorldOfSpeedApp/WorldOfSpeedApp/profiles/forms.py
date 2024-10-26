from django import forms

from WorldOfSpeedApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()


class ProfileCreateForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):
        fields = ['username', 'email', 'age', 'password']


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        labels = {
            'image_url': 'Profile Picture'
        }


class ProfileDeleteForm(ProfileBaseForm):
    pass
