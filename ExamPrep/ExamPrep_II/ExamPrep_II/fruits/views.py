from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from ExamPrep_II.fruits.forms import FruitCreateForm
from ExamPrep_II.fruits.models import Fruit
from ExamPrep_II.utils import get_user_obj


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class FruitDetailsView(DetailView):
    model = Fruit
    pk_url_kwarg = 'fruitId'
    template_name = 'fruits/details-fruit.html'


class FruitEditView(UpdateView):
    model: Fruit
    pk_url_kwarg = 'fruitId'
    template_name = 'fruits/edit-fruit.html'

