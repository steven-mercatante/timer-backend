from django.db import models
from django.conf import settings
from projects.models import Project


class Entry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    seconds = models.IntegerField()
    running = models.BooleanField(default=False)
    logged_for = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
