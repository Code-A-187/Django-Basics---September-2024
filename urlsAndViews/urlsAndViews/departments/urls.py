from django.urls import path

from urlsAndViews.departments import views
from urlsAndViews.departments.views import index

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<int:pk>/<slug:slug>/', views.view_with_slug),
    path('<variable>/', views.view_with_name),  # matches till /
    path('<path:variable>', views.view_with_name),  # matches after as well
    # path('<uuid:id>/', some,view)
    # path('<param>/', views.view_with_args_kwargs),
]
