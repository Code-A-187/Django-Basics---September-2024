from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.utils import get_user_obj


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarDetailsView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'cars/car-details.html'


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = 'cars/car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

