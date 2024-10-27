from django.shortcuts import render
from django.views.generic import ListView

from FurryFunniesApp.posts.models import Post


def index_view(request):
    return render(request, 'index.html')


class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'
