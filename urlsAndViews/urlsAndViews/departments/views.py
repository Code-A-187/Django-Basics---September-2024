from django.http import HttpResponse
from django.shortcuts import render

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')


def view_with_name(request, variable):
    # should be named same as in the urls (can get it with variables or args and kwargs)
    return HttpResponse(f'<h1>Variable: {variable}</h1>')


def view_with_args_kwargs(request, *args, **kwargs):
    # should be named same as in the urls (can get it with variables or args and kwargs)
    return HttpResponse(f'<h1>Args: {args}, Kwargs {kwargs}</h1>')


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>')


def view_with_slug(request, pk, slug):
    department = Department.objects.get(pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")