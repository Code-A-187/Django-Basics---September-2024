from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView, CreateView
from ExamPrep_II.profiles.forms import ProfileCreateForm
from ExamPrep_II.profiles.models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
