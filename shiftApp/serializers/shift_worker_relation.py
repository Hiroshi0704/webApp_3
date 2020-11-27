from rest_framework import serializers

from .shift import ShiftSerializer
from .worker import WorkerSerializer
from ..models import ShiftWorkerRelation


class WorkerRelationSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer()
    worker = WorkerSerializer()

    class Meta:
        model = ShiftWorkerRelation
        fields = ['id', 'total_time', 'shift', 'worker', 'app']
