"""
STEP 1: Create a project
STEP 2: Create an app
STEP 3: Add the app to INSTALlED_APPS

"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
