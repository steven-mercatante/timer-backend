from django.views.generic import TemplateView


class AuthSuccess(TemplateView):
  template_name = 'auth_success.html'
