import uuid

from django.core.validators import MinValueValidator
from django.db import models

from .shift import Shift
from .shift_app import ShiftApp
from .worker import Worker


class ShiftWorkerRelation(models.Model):
    """勤務表と従業員を紐付けるクラス
    従業員の勤務時間を保持するために必要
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_time = models.FloatField(validators=[MinValueValidator(0)])
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.shift}] {self.worker}: {self.total_time}'
