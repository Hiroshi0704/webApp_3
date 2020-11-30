from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from shiftapp.serializers import ShiftAppSerializer
from shiftapp.models import ShiftApp
from shiftapp.permissions import IsOwner


class ShiftAppViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftAppSerializer
    queryset = ShiftApp.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
