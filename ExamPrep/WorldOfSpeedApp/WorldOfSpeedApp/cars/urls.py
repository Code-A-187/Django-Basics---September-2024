from django.urls import path, include

from WorldOfSpeedApp.cars import views

urlpatterns = [
    path('create/', views.CarCreateView.as_view(), name='car-create'),
    path('<int:id>', include([
        path('details/', views.CarDetailsView.as_view(), name='car-details'),
        path('edit/', views.CarEditView.as_view(), name='car-edit'),
        path('delete/', views.CarDeleteView.as_view(), name='car-delete'),
    ]))
]
