from django.contrib import admin
from djangointro.todo_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
    
