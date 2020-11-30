from rest_framework import viewsets

from shiftapp.serializers import WorkScheduleSerializer
from shiftapp.models import WorkSchedule


class WorkScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = WorkScheduleSerializer
    queryset = WorkSchedule.objects.all()
