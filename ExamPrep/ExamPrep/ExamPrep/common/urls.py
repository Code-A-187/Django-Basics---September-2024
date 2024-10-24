from django.urls import path

from ExamPrep.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]

