from rest_framework import serializers

from .work_style import WorkStyleSerializer
from ..models import WorkSchedule


class WorkScheduleSerializer(serializers.ModelSerializer):
    # shift = ShiftSerializer()
    work_style = WorkStyleSerializer()

    class Meta:
        model = WorkSchedule
        fields = [
            'id',
            'date',
            'is_rest_request',
            'work_style',
            'worker',
            'shift',
            'app'
        ]
