from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')


def view_with_name(request, *args, **kwargs):
    return HttpResponse(f'<h1>Args: {args}, Kwargs: {kwargs}</h1>')

