from rest_framework import serializers

from .shift_app import ShiftAppSerializer
from ..models import ShiftAppWorkerInvitation


class ShiftAppWorkerInvitationSerializer(serializers.ModelSerializer):
    inviter = ShiftAppSerializer()
    invitee = ShiftAppSerializer()

    class Meta:
        model = ShiftAppWorkerInvitation
        fields = ['id', 'inviter', 'invitee', 'expired_by']

    def validate(self, attrs):
        if attrs['inviter'] == attrs['invitee']:
            raise serializers.ValidationError("You can't invite yourself")
        return attrs
