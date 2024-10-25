from django.urls import path

from ExamPrep_II.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
]