from django.urls import reverse_lazy
from django.views.generic import CreateView

from WorldOfSpeedApp.profiles.forms import ProfileCreateForm
from WorldOfSpeedApp.profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
