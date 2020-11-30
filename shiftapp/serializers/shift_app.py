from rest_framework import serializers

from .shift_app_plan import ShiftAppPlanSerializer
from ..models import ShiftApp


class ShiftAppSerializer(serializers.ModelSerializer):
    plan_info = ShiftAppPlanSerializer(read_only=True, source='plan')

    class Meta:
        model = ShiftApp
        fields = ['id', 'user', 'plan', 'plan_info']
        read_only_fields = ['user']
