from .models import Entry
from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'project', 'task', 'notes', 'seconds', 'logged_for']
