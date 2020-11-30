from rest_framework import viewsets

from shiftapp.serializers import WorkPlanSerializer
from shiftapp.models import WorkPlan


class WorkPlanViewSet(viewsets.ModelViewSet):
    serializer_class = WorkPlanSerializer
    queryset = WorkPlan.objects.all()
