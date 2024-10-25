from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ExamPrep_II.common.urls')),
    # path('fruit/', include('ExamPrep_II.fruits.urls')),
    # path('profile/', include('ExamPrep_II.profiles.urls'))
]
