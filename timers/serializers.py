from .models import Timer
from rest_framework import serializers


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['id', 'project', 'task', 'running', 'starts', 'stops']
