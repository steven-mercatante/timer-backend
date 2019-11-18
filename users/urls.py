from django.urls import path
from . import views


urlpatterns = [
    path('users/auth-success', views.auth_success, name='auth-success'),
    path('users/logout', views.LogOutView.as_view(), name='log_out'),
]
