from django.db import models
from django.conf import settings
from projects.models import Project


class Timer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    running = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TimerStart(models.Model):
    """Tracks any time a timer was started."""
    timer = models.ForeignKey(
        Timer,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


class TimerStop(models.Model):
    """Tracks any time a timer was stopped."""
    timer = models.ForeignKey(
        Timer,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
