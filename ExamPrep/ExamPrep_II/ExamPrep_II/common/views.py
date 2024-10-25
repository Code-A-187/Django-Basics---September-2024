from django.shortcuts import render
from django.views.generic import ListView
from ExamPrep_II.fruits.models import Fruit


def index(request):
    return render(request, 'index.html')


class DashboardView(ListView):
    model = Fruit
    template_name = 'dashboard.html'

