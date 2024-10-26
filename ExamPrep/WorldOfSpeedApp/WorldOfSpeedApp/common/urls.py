from django.urls import path

from WorldOfSpeedApp.common import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue')
]