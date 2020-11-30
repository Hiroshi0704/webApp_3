from rest_framework import serializers

from shiftapp.models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    # worker_detail = UserSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'worker_detail', 'hourlyWage', 'app']
