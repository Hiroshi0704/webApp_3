from rest_framework import serializers

from .user import UserSerializer
from ..models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    worker_detail = UserSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'worker_detail', 'hourlyWage', 'app']
