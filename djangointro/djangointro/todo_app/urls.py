from django.urls import path
from djangointro.todo_app.views import index

urlpatterns = [
    path('', index),
]