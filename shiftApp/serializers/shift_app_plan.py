from rest_framework import serializers

from ..models import ShiftAppPlan


class ShiftAppPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShiftAppPlan
        fields = ['title', 'price', 'is_manager', 'max_worker']
