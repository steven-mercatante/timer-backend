from django.http import HttpResponse
from django.template import loader
from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.tokens import RefreshToken


def auth_success(request):
    # refresh_token = RefreshToken.for_user(request.user)
    # token = {
    #     "refresh": str(refresh_token),
    #     "access": str(refresh_token.access_token),
    # }
    token = Token.objects.get(user_id=request.user.id)
    template = loader.get_template('auth_success.html')

    resp = HttpResponse(template.render({}, request))
    resp.set_cookie('auth_token', str(token))

    return resp
