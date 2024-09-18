from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    return HttpResponse('<h1>Main View!</h1>')
def add_view(request):
    return HttpResponse('<h1>Add View!</h1>')