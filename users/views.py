from django.http import HttpResponse
from django.template import loader
from rest_framework.authtoken.models import Token


def auth_success(request):
    token = Token.objects.get(user_id=request.user.id)
    template = loader.get_template('auth_success.html')

    resp = HttpResponse(template.render({}, request))
    resp.set_cookie('auth_token', str(token))

    return resp
