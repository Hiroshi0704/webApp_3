from rest_framework import serializers

from .worker import WorkerSerializer
from ..models import Shift, Worker


class ShiftSerializer(serializers.ModelSerializer):
    worker_info = WorkerSerializer(many=True, read_only=True, source='worker')
    worker = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Worker.objects.all())

    class Meta:
        model = Shift
        fields = ['id', 'title', 'start_date', 'end_date', 'created_at',
                  'updated_at', 'worker', 'worker_info', 'is_public', 'app']
        extra_kwargs = {
            'app': {'read_only': True},
        }
