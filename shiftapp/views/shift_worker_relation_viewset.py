from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from shiftapp.models import ShiftWorkerRelation
from shiftapp.serializers import ShiftWorkerRelationSerializer


class ShiftWorkerRelationViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftWorkerRelationSerializer
    queryset = ShiftWorkerRelation.objects.all()
    permission_classes = [IsAuthenticated]
