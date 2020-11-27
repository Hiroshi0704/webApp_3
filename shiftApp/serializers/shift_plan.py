from rest_framework import serializers

from ..models import ShiftPlan


class ShiftPlanSerializer(serializers.ModelSerializer):
    # work_plan = WorkPlanSerializer()
    # shift = ShiftSerializer()

    class Meta:
        model = ShiftPlan
        fields = ['id', 'date', 'work_plan', 'shift', 'app']
