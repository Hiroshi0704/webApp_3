from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from shiftApp.serializers import ShiftSerializer
from shiftApp.models import Shift, ShiftApp


class ShiftViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftSerializer
    queryset = Shift.objects.all()

    def perform_create(self, serializer):
        app = get_object_or_404(ShiftApp, user=self.request.user)
        serializer.save(app=app)
