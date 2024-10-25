from django.urls import path
from ExamPrep_II.fruits import views

urlpatterns = [
    path('create/', views.FruitCreateView.as_view(), name='fruit-create')
]