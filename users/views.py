from django.http import HttpResponse
from django.template import loader
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response


def auth_success(request):
    try:
        token = Token.objects.get(user_id=request.user.id)
    except Token.DoesNotExist:
        token = Token.objects.create(user=request.user)
    template = loader.get_template('auth_success.html')

    resp = HttpResponse(template.render({}, request))
    resp.set_cookie('auth_token', str(token))

    return resp


class LogOutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        resp = Response('logged out')
        resp.delete_cookie('auth_token')
        return resp
