from django.shortcuts import render
from djangointro.todo_app.models import Task


def index(request):
    title_filter = request.GET.get('title_filter', '')
    if title_filter:
        tasks = Task.objects.filter(name__icontains=title_filter)
    else:
        tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/index.html', context)
