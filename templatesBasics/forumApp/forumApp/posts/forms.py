from django import forms

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(PostBaseForm):
        pass


class PostEditForm(PostBaseForm):
        pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


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