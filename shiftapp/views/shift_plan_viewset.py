from rest_framework import viewsets

from shiftapp.serializers import ShiftPlanSerializer
from shiftapp.models import ShiftPlan


class ShiftPlanViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftPlanSerializer
    queryset = ShiftPlan.objects.all()
