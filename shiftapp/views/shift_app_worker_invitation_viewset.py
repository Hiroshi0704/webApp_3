from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from shiftapp.serializers import ShiftAppWorkerInvitationSerializer
from shiftapp.models import ShiftAppWorkerInvitation, ShiftApp


class ShiftAppWorkerInvitationViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftAppWorkerInvitationSerializer
    queryset = ShiftAppWorkerInvitation.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        inviter = serializer.context.get('inviter')
        serializer.save(inviter=inviter)

    def get_serializer_context(self):
        inviter = get_object_or_404(ShiftApp, user=self.request.user)
        context = {
            'request': self.request,
            'inviter': inviter,
        }
        return context
