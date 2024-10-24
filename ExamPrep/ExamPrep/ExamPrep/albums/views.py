from django.urls import reverse_lazy
from django.views.generic import CreateView

from ExamPrep.albums.forms import AlbumCreateForm
from ExamPrep.albums.models import Album
from ExamPrep.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


