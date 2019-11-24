from rest_framework import exceptions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Timer, TimerStart, TimerStop
from .serializers import (
    TimerSerializer, TimerStartSerializer, TimerStopSerializer
)


class TimerViewSet(viewsets.ModelViewSet):
    serializer_class = TimerSerializer

    def get_queryset(self):
        return Timer.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def find_timer(request):
    try:
        timer_id = pk = request.data['timer']
    except KeyError:
        raise exceptions.ValidationError('`timer` argument is required')

    try:
        return Timer.objects.get(pk=timer_id)
    except Timer.DoesNotExist:
        raise exceptions.ValidationError(
            f'Timer with ID {timer_id} not found')


class TimerStartView(APIView):
    def post(self, request):
        timer = find_timer(request)
        timer_start = TimerStart.objects.create(timer=timer)
        return Response(TimerStartSerializer(timer_start).data)


class TimerStopView(APIView):
    def post(self, request):
        timer = find_timer(request)
        timer_stop = TimerStop.objects.create(timer=timer)
        return Response(TimerStopSerializer(timer_stop).data)
