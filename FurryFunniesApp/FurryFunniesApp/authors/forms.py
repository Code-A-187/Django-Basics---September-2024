from django import forms

from FurryFunniesApp.authors.models import Author
from FurryFunniesApp.mixins import PlaceholderMixin


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(PlaceholderMixin, AuthorBaseForm):
    placeholders = {
        "first_name": "Enter your first name...",
        "last_name": "Enter your last name...",
        "pets_number": "Enter the number of your pets...",
    }

    class Meta(AuthorBaseForm.Meta):
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "pets_number": "Pets Number",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['passcode'].widget = forms.PasswordInput(
            attrs={
                'placeholder': "Enter 6 digits..."
            }
        )


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):

        exclude = ['passcode']
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "pets_number": "Pets Number",
            "image_url": "Profile Image URL"
        }
