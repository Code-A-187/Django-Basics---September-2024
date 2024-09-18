"""
STEP 1: Create a project
STEP 2: Create an app
STEP 3: Add the app to INSTALlED_APPS
STEP 4: Replace DB settings with Postgres DB settings
STEP 5: Enter credentials
STEP 6: Install psycopg2
STEP 7: Create data base
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include("djangointro.todo_app.urls"))
]
