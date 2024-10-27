from django import forms

from FurryFunniesApp.mixins import PlaceholderMixin, ReadOnlyMixin
from FurryFunniesApp.posts.models import Post


class PostBaseForm(PlaceholderMixin, forms.ModelForm):
    placeholders = {
        'title': "Put an attractive and unique title...",
        'content': "Share some interesting facts about your adorable pets...",
    }

    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'image_url': "Post Image URL"
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True