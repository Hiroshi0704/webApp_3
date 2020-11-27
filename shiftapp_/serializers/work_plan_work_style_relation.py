from rest_framework import serializers

from .work_plan import WorkPlanSerializer
from .work_style import WorkStyleSerializer
from ..models import WorkPlanWorkStyleRelation


class WorkPlanWorkStyleRelationSerializer(serializers.ModelSerializer):
    work_plan = WorkPlanSerializer()
    work_style = WorkStyleSerializer()

    class Meta:
        model = WorkPlanWorkStyleRelation
        fields = ['id', 'work_plan', 'work_style', 'work_style_num']
