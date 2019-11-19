from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('clients.urls')),
    path('', include('projects.urls')),
    path('', include('timers.urls')),
    path('', include('timesheets.urls')),
    path('', include('users.urls')),
]
