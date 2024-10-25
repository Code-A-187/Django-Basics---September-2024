from django import forms

from ExamPrep_II.mixins import PlaceholderMixin, NoLabelMixin
from ExamPrep_II.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(PlaceholderMixin, NoLabelMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['age', 'image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        )


class ProfileEditForm(PlaceholderMixin, NoLabelMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['password']
