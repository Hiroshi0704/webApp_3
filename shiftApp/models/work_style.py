import uuid

from django.db import models

from .shift_app import ShiftApp


class WorkStyle(models.Model):
    """勤務形態"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    symbol = models.CharField(max_length=1)
    start_time = models.TimeField()
    break_time = models.TimeField()
    end_time = models.TimeField()
    is_night = models.BooleanField(default=False)
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.symbol
