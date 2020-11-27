import uuid

from django.db import models

from .shift import Shift
from .shift_app import ShiftApp
from .worker import Worker
from .work_style import WorkStyle


class WorkSchedule(models.Model):
    """従業員の勤務予定"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    is_rest_request = models.BooleanField(default=False)
    work_style = models.ForeignKey(
        WorkStyle, on_delete=models.CASCADE, blank=True, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.date}] {self.worker}: {self.work_style}'
