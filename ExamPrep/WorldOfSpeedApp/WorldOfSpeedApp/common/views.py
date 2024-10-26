from django.shortcuts import render
from django.views.generic import ListView

from WorldOfSpeedApp.cars.models import Car


def index_view(request, *args, **kwargs):
    return render(request, 'index.html')


class CatalogueView(ListView):
    model = Car
    template_name = 'catalogue.html'
