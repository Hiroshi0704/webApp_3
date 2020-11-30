from rest_framework import viewsets

from shiftapp.serializers import WorkerSerializer
from shiftapp.models import Worker


class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
