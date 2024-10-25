from django.urls import path, include
from ExamPrep_II.fruits import views

urlpatterns = [
    path('create/', views.FruitCreateView.as_view(), name='fruit-create'),
    path('<int:fruitId>/', include([
        path('details/', views.FruitDetailsView.as_view(), name='fruit-details'),
        path('edit/', views.FruitEditView.as_view(), name='fruit-edit')
    ]))
]