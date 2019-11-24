from .models import Timer, TimerStart, TimerStop
from rest_framework import serializers


class TimerSerializer(serializers.ModelSerializer):
    starts = serializers.SerializerMethodField()
    stops = serializers.SerializerMethodField()

    def get_starts(self, obj):
        return [
            int(t.timestamp())
            for t
            in TimerStart.objects.filter(timer=obj.id).values_list('created_at', flat=True)
        ]

    def get_stops(self, obj):
        return [
            int(t.timestamp())
            for t
            in TimerStop.objects.filter(timer=obj.id).values_list('created_at', flat=True)
        ]

    class Meta:
        model = Timer
        fields = ['id', 'project', 'task', 'running', 'starts', 'stops']


class TimerStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerStart
        fields = ['created_at']


class TimerStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerStop
        fields = ['created_at']
