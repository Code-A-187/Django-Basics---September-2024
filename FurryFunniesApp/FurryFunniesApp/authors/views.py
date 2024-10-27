from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from FurryFunniesApp.authors.forms import AuthorCreateForm, AuthorEditForm
from FurryFunniesApp.authors.models import Author
from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.utils import get_author_obj


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dash')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthorDetailsView(DetailView):
    model = Post
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_author_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts_count'] = self.object.posts.count()

        context['last_updated_post'] = self.object.posts.order_by('updated_at').last()

        return context


class AuthorEditView(UpdateView):
    model = Post
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_author_obj()


class AuthorDeleteView(DeleteView):
    model = Post
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author_obj()
