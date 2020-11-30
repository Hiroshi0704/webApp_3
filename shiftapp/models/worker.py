import uuid

from django.core.validators import MinValueValidator
from django.db import models

from .shift_app import ShiftApp


class Worker(models.Model):
    """従業員"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    worker_detail = models.ForeignKey(
        ShiftApp, on_delete=models.CASCADE, related_name='worker_detail')
    hourlyWage = models.FloatField(validators=[MinValueValidator(0)])
    app = models.ForeignKey(ShiftApp, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.worker_detail}'
