from django.urls import path
from . import views


urlpatterns = [
  path('users/auth-success', views.AuthSuccess.as_view(), name='auth-success'),
]
