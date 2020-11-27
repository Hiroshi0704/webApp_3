import uuid

from django.db import models

from .shift_app import ShiftApp


class WorkPlan(models.Model):
    """1日の勤務計画"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
