from rest_framework import viewsets

from shiftapp.models import WorkStyle
from shiftapp.serializers import WorkStyleSerializer


class WorkStyleViewSet(viewsets.ModelViewSet):
    serializer_class = WorkStyleSerializer
    queryset = WorkStyle.objects.all()
