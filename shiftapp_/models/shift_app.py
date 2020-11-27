import uuid

from django.contrib.auth import get_user_model
from django.db import models

from .shift_app_plan import ShiftAppPlan


class ShiftApp(models.Model):
    """勤務表作成機能"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    plan = models.ForeignKey(
        ShiftAppPlan, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f'ShiftApp [{self.user.username}]'
