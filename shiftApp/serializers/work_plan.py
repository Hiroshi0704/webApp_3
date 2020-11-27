from rest_framework import serializers

from ..models import WorkPlan


class WorkPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkPlan
        fields = ['id', 'title', 'app']
