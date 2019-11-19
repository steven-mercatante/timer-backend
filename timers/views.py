from rest_framework import viewsets
from .models import Timer
from .serializers import TimerSerializer


class TimerViewSet(viewsets.ModelViewSet):
    serializer_class = TimerSerializer

    def get_queryset(self):
        return Timer.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
