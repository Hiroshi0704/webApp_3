from rest_framework import serializers

from ..models import WorkStyle


class WorkStyleSerializer(serializers.ModelSerializer):
    # app = ShiftAppSerializer()

    class Meta:
        model = WorkStyle
        fields = [
            'id',
            'symbol',
            'start_time',
            'break_time',
            'end_time',
            'is_night',
            'app',
        ]
        extra_kwargs = {
            'app': {'read_only': True},
        }
