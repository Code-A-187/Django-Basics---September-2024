from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WorldOfSpeedApp.common.urls')),
    path('profile/', include('WorldOfSpeedApp.profiles.urls'))
]
