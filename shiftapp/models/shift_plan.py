import uuid

from django.db import models

from .shift import Shift
from .shift_app import ShiftApp
from .work_plan import WorkPlan


class ShiftPlan(models.Model):
    """勤務表の計画"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    work_plan = models.ForeignKey(
        WorkPlan, on_delete=models.CASCADE, blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self):
        if self.work_plan:
            return f'[{self.date}] {self.work_plan.title}'
        else:
            return f'[{self.date}] {self.work_plan}'
