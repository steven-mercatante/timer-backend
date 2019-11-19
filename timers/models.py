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
    # TODO: use array or json field once I switch to Postgres
    # TODO: might want to initialize with current time when creating new record
    starts = models.TextField(default="[]")
    # TODO: use array or json field once I switch to Postgres
    stops = models.TextField(default="[]")
    running = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
