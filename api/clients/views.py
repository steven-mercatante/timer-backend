from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all() # TODO: limit to currently auth'd user
  serializer_class = ClientSerializer
