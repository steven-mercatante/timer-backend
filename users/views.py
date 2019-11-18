from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken


def auth_success(request):
    refresh_token = RefreshToken.for_user(request.user)
    token = {
        "refresh": str(refresh_token),
        "access": str(refresh_token.access_token),
    }
    return render(request, 'auth_success.html')
