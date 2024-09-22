from django.urls import path

from urlsAndViews.departments import views
from urlsAndViews.departments.views import index

urlpatterns = [
    path('', views.index),
    path('<param>/', views.view_with_name)
]