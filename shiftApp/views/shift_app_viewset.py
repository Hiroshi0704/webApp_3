from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from shiftapp.serializers import ShiftAppSerializer
from shiftapp.models import ShiftApp


class ShiftAppViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftAppSerializer
    queryset = ShiftApp.objects.all()

    # def perform_create(self, serializer):
    #     app = get_object_or_404(ShiftApp, user=self.request.user)
    #     serializer.save(app=app)
