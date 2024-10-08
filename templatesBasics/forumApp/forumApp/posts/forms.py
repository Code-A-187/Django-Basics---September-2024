from django import forms

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        error_messages = {
            'title': {
                'required': 'Please enter the title of your post',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters'
            },
            'author': {
                'required': 'Please enter an author'
            }
        }


class PostCreateForm(PostBaseForm):
        pass


class PostEditForm(PostBaseForm):
        pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...'
            }
        )
    )

        # widgets = {
        #     "title": forms.NumberInput,
        # }
        #
        # labels = {
        #     "title": "That's a title label"
        # }
        #
        # help_texts = {
        #     'title': 'This is the title'
        # }


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#     )
#
#     content = forms .CharField(
#         widget=forms.Textarea,
#     )
#
#     author = forms.CharField(
#         max_length=30,
#     )
#
#     created_at = forms.DateTimeField(
#         auto_now_add=True
#     )
#
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices
#
#     )