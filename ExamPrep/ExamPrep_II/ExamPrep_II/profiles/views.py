from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from ExamPrep_II.profiles.forms import ProfileCreateForm, ProfileEditForm
from ExamPrep_II.profiles.models import Profile
from ExamPrep_II.utils import get_user_obj


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
