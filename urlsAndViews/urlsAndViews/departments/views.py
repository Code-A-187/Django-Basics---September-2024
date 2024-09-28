import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')


def view_with_name(request, variable):
    # should be named same as in the urls (can get it with variables or args and kwargs)
    # return HttpResponse(f'<h1>Variable: {variable}</h1>')
    return render(request,'departments/name_template.html', {'variable': variable})



def view_with_args_kwargs(request, *args, **kwargs):
    # should be named same as in the urls (can get it with variables or args and kwargs)
    return HttpResponse(f'<h1>Args: {args}, Kwargs {kwargs}</h1>')


def view_with_int_pk(request, pk):
    # return HttpResponse(json.dumps({"pk": pk}), content_type="application/json")
    return JsonResponse({"pk":pk})  #  under the hood makes json.dumps as shown above


def view_with_slug(request, pk, slug):
    department = Department.objects.get(pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request,archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}")