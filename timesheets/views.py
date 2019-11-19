from rest_framework import viewsets
from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
