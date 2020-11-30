from rest_framework import serializers

from shiftapp.models import ShiftAppWorkerInvitation
from .shift_app import ShiftAppSerializer


class ShiftAppWorkerInvitationSerializer(serializers.ModelSerializer):
    inviter = ShiftAppSerializer(read_only=True)
    # invitee = serializers.PrimaryKeyRelatedField(
    #     read_only=False, queryset=ShiftApp.objects.all())

    class Meta:
        model = ShiftAppWorkerInvitation
        fields = ['id', 'inviter', 'invitee', 'expired_by']

    def validate(self, attrs):
        inviter = self.context.get('inviter')
        if inviter == attrs['invitee']:
            raise serializers.ValidationError("You can't invite yourself")
        return attrs
