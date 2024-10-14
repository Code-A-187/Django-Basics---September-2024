from django.urls import path, include

from forumApp.posts import views
from forumApp.posts.views import Index, IndexView, RedirectHomeView, DashboardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dash'),
    path('add-post/', views.add_post, name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', views.delete_post, name='delete-post'),
        path('details-post/', views.details_page, name='details-post'),
        path('edit-post', views.edit_post, name='edit-post')
    ])),
    path('redirect-home/', RedirectHomeView.as_view(), name='redirect-home')

]
