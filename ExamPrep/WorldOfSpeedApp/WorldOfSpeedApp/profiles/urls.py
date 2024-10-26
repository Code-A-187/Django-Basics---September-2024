from django.urls import path
from WorldOfSpeedApp.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='profile-create')
]