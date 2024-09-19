from django.shortcuts import render
from djangointro.todo_app.models import Task


def index(request):
    tasks = Task.objects.all()

    result = '\n'.join([
        '<h1>TASKS</h1>',
        '<ul>',
        *[f"<li>{task.name}</li>" for task in tasks],
        '</ul>',
    ])
    return render(request, 'tasks/index.html')
