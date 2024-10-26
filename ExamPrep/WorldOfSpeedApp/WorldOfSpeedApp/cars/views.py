from django.urls import reverse_lazy
from django.views.generic import CreateView

from WorldOfSpeedApp.cars.forms import CarCreateForm
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

