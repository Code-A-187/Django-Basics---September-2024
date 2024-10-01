from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        'current_time': datetime.now(),
        "person": {
            "age": 20,
            'height': 200,
        },
        'ids': ['q345765w343', 'r3r3rwer46375666', '32wq34q235qt'],
        'some_text': 'Hello',
        "users": [
            "Pesho",
            "Ivan",
            "Pancho",
            "Gabriela",
            "Mihaela"
        ]
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project 1",
                "author": "Anton Simeonov",
                "content": "I **really** don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2",
                "author": "",
                "content": "### I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 3",
                "author": "Anton Simeonov",
                "content": "",
                "created_at": datetime.now(),
            },
    ]
    }

    return render(request, 'posts/dashboard.html', context)
