from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from WorldOfSpeedApp.profiles.models import Profile
from WorldOfSpeedApp.utils import get_user_obj


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.get_object()

        total_price = Car.objects.filter(owner=profile).aggregate(Sum('price'))['price__sum'] or 0
        context['total_price'] = round(total_price, 3)

        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
