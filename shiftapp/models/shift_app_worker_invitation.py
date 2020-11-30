import datetime
import uuid

from django.db import models

from .shift_app import ShiftApp


class ShiftAppWorkerInvitation(models.Model):
    """勤怠管理機能の従業員招待で使用する情報を保持するクラス"""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    inviter = models.ForeignKey(
        ShiftApp, on_delete=models.CASCADE, related_name='inviter')

    invitee = models.ForeignKey(
        ShiftApp, on_delete=models.CASCADE, related_name='invitee')

    expired_by = models.DateField()

    def is_expired(self):
        return datetime.now() > self.expired_by
