from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from FurryFunniesApp.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.utils import get_author_obj


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dash')

    def form_valid(self, form):
        form.instance.author = get_author_obj()
        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'id'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dash')


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
